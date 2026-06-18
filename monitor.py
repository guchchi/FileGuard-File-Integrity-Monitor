import json
import os

from hasher import scan_folder

BASELINE_FILE = "baseline.json"
MONITORED_DIR = "monitored_files"


def load_baseline():
    """Load saved baseline hashes from baseline.json."""
    if not os.path.exists(BASELINE_FILE):
        return {}
    with open(BASELINE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_baseline(baseline_data):
    """Save baseline hashes to baseline.json."""
    with open(BASELINE_FILE, "w", encoding="utf-8") as f:
        json.dump(baseline_data, f, indent=2)
    print(f"  [OK] Baseline saved to {BASELINE_FILE}")


def compare_baseline():
    """Compare current file hashes against the saved baseline.

    Returns a dictionary with:
        unchanged, modified, new_files, deleted, current_hashes
    """
    baseline = load_baseline()
    if not baseline:
        print("  [ERROR] No baseline found. Run --baseline first.")
        return None

    current_hashes = scan_folder(MONITORED_DIR)

    unchanged = {}
    modified = {}
    new_files = {}
    deleted = {}

    baseline_paths = set(baseline.keys())
    current_paths = set(current_hashes.keys())

    # Files that still exist — check if hash matches baseline
    common_paths = baseline_paths & current_paths
    for path in common_paths:
        if baseline[path] == current_hashes[path]:
            unchanged[path] = current_hashes[path]
        else:
            modified[path] = {
                "expected": baseline[path],
                "current": current_hashes[path],
            }

    # Files in baseline but not on disk
    for path in baseline_paths - current_paths:
        deleted[path] = baseline[path]

    # Files on disk but not in baseline
    for path in current_paths - baseline_paths:
        new_files[path] = current_hashes[path]

    return {
        "unchanged": unchanged,
        "modified": modified,
        "new_files": new_files,
        "deleted": deleted,
        "current_hashes": current_hashes,
        "baseline": baseline,
    }

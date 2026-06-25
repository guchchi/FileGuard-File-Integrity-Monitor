import json
import os
from typing import Any, Dict, Optional

from hasher import scan_folder

BASELINE_FILE = "baseline.json"
MONITORED_DIR = "monitored_files"

ComparisonResult = Dict[str, Any]


def load_baseline() -> Dict[str, str]:
    if not os.path.exists(BASELINE_FILE):
        return {}
    with open(BASELINE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_baseline(baseline_data: Dict[str, str]) -> None:
    with open(BASELINE_FILE, "w", encoding="utf-8") as f:
        json.dump(baseline_data, f, indent=2)
    print(f"  [OK] Baseline saved to {BASELINE_FILE}")


def compare_baseline() -> Optional[ComparisonResult]:
    baseline = load_baseline()
    if not baseline:
        print("  [ERROR] No baseline found. Run --baseline first.")
        return None

    current_hashes = scan_folder(MONITORED_DIR)

    unchanged: Dict[str, str] = {}
    modified: Dict[str, Dict[str, str]] = {}
    new_files: Dict[str, str] = {}
    deleted: Dict[str, str] = {}

    baseline_paths = set(baseline.keys())
    current_paths = set(current_hashes.keys())

    common_paths = baseline_paths & current_paths
    for path in common_paths:
        if baseline[path] == current_hashes[path]:
            unchanged[path] = current_hashes[path]
        else:
            modified[path] = {
                "expected": baseline[path],
                "current": current_hashes[path],
            }

    for path in baseline_paths - current_paths:
        deleted[path] = baseline[path]

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

"""FileGuard — File Integrity Monitoring Tool

Monitors file integrity using SHA-256 hashes, detects file changes,
and generates tamper-detection reports.

Usage:
    python main.py --baseline    Create initial hash baseline
    python main.py --check       Compare current files against baseline
"""

import argparse
import os
import sys
from typing import NoReturn

from hasher import scan_folder
from monitor import save_baseline, compare_baseline
from report import (
    generate_report_data,
    print_terminal_report,
    save_text_report,
    save_json_report,
)

MONITORED_DIR = "monitored_files"
REPORTS_DIR = "reports"
TEXT_REPORT = os.path.join(REPORTS_DIR, "integrity_report.txt")
JSON_REPORT = os.path.join(REPORTS_DIR, "integrity_report.json")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="FileGuard — File Integrity Monitoring Tool"
    )
    parser.add_argument(
        "--baseline",
        action="store_true",
        help="Create a baseline of file hashes for monitored_files/",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check current file integrity against the saved baseline",
    )
    args = parser.parse_args()

    if not args.baseline and not args.check:
        parser.print_help()
        print()
        print("  Example:")
        print("    python main.py --baseline    Create baseline")
        print("    python main.py --check       Check integrity")
        return

    if args.baseline:
        _create_baseline()

    if args.check:
        _run_integrity_check()


def _create_baseline() -> None:
    print("FileGuard — creating baseline...")
    print()

    if not os.path.isdir(MONITORED_DIR):
        print(f"  [ERROR] {MONITORED_DIR}/ directory not found.")
        return

    hashes = scan_folder(MONITORED_DIR)
    if not hashes:
        print("  [ERROR] No files found to baseline.")
        return

    print(f"  Scanned {len(hashes)} file(s) in {MONITORED_DIR}/")
    for path in sorted(hashes.keys()):
        print(f"    {path}: {hashes[path][:16]}...")

    save_baseline(hashes)
    print()
    print("FileGuard — baseline created successfully.")
    print(f"  Run 'python main.py --check' to verify integrity.")


def _run_integrity_check() -> None:
    print("FileGuard — checking integrity...")
    print()

    comparison = compare_baseline()
    if comparison is None:
        return

    unchanged_count = len(comparison["unchanged"])
    modified_count = len(comparison["modified"])
    new_count = len(comparison["new_files"])
    deleted_count = len(comparison["deleted"])

    total_baseline = len(comparison["baseline"])
    total_current = len(comparison["current_hashes"])

    print(f"  Baseline: {total_baseline} file(s)")
    print(f"  Current:  {total_current} file(s)")
    print(f"  Unchanged: {unchanged_count}   Modified: {modified_count}")
    print(f"  New: {new_count}   Deleted: {deleted_count}")
    print()

    report_data = generate_report_data(comparison)
    print_terminal_report(report_data)

    os.makedirs(REPORTS_DIR, exist_ok=True)
    save_text_report(report_data, TEXT_REPORT)
    save_json_report(report_data, JSON_REPORT)

    print()
    print("FileGuard — integrity check complete.")


if __name__ == "__main__":
    main()

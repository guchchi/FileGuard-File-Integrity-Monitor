import json
from datetime import datetime
from typing import Any, Dict, List

from monitor import ComparisonResult

ReportData = Dict[str, Any]


def generate_report_data(comparison_result: ComparisonResult) -> ReportData:
    total_scanned = len(comparison_result["current_hashes"])
    unchanged_count = len(comparison_result["unchanged"])
    modified_count = len(comparison_result["modified"])
    new_count = len(comparison_result["new_files"])
    deleted_count = len(comparison_result["deleted"])
    severity = _calculate_severity(modified_count, deleted_count, new_count)

    return {
        "report_title": "FileGuard Integrity Report",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "total_files_scanned": total_scanned,
            "unchanged_files": unchanged_count,
            "modified_files": modified_count,
            "new_files": new_count,
            "deleted_files": deleted_count,
            "severity": severity,
        },
        "details": {
            "unchanged": list(comparison_result["unchanged"].keys()),
            "modified": list(comparison_result["modified"].keys()),
            "new_files": list(comparison_result["new_files"].keys()),
            "deleted": list(comparison_result["deleted"].keys()),
        },
        "recommended_actions": _get_recommendations(
            modified_count, deleted_count, new_count
        ),
    }


def _calculate_severity(
    modified_count: int, deleted_count: int, new_count: int
) -> str:
    if deleted_count > 0 or modified_count > 1:
        return "High"
    if modified_count == 1:
        return "Medium"
    if new_count > 0:
        return "Low"
    return "None"


def _get_recommendations(
    modified_count: int, deleted_count: int, new_count: int
) -> List[str]:
    actions: List[str] = []

    if modified_count > 0:
        actions.append("Review the modified files for unauthorized changes")
        actions.append("Compare modified files with known backups")

    if deleted_count > 0:
        actions.append("Investigate why files were deleted")
        actions.append("Restore deleted files from backup if needed")
        actions.append("Verify whether deletion was authorized")

    if new_count > 0:
        actions.append("Review newly added files for legitimacy")

    actions.append("Continue monitoring sensitive directories")
    actions.append("Maintain secure backups of critical files")
    actions.append("Investigate unexpected file system changes")

    return actions


def print_terminal_report(report_data: ReportData) -> None:
    s = report_data["summary"]

    print("=" * 50)
    print("FileGuard Integrity Report".center(50))
    print("=" * 50)
    print(f"  Generated:              {report_data['generated_at']}")
    print(f"  Total Files Scanned:    {s['total_files_scanned']}")
    print(f"  Unchanged Files:        {s['unchanged_files']}")
    print(f"  Modified Files:         {s['modified_files']}")
    print(f"  New Files:              {s['new_files']}")
    print(f"  Deleted Files:          {s['deleted_files']}")
    print(f"  Severity:               {s['severity']}")
    print()

    if s["modified_files"] > 0:
        print("  Modified Files:")
        for f in report_data["details"]["modified"]:
            print(f"    * {f}")
        print()

    if s["deleted_files"] > 0:
        print("  Deleted Files:")
        for f in report_data["details"]["deleted"]:
            print(f"    * {f}")
        print()

    if s["new_files"] > 0:
        print("  New Files:")
        for f in report_data["details"]["new_files"]:
            print(f"    * {f}")
        print()

    print("-" * 50)
    print("Recommended Actions".center(50))
    print("-" * 50)
    for action in report_data["recommended_actions"]:
        print(f"  * {action}")
    print()
    print("=" * 50)


def save_text_report(report_data: ReportData, filepath: str) -> None:
    s = report_data["summary"]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("  FileGuard Integrity Report\n")
        f.write("=" * 60 + "\n")
        f.write(f"  Generated: {report_data['generated_at']}\n")
        f.write("\n")
        f.write("-" * 60 + "\n")
        f.write("  Summary\n")
        f.write("-" * 60 + "\n")
        f.write(f"  Total Files Scanned:    {s['total_files_scanned']}\n")
        f.write(f"  Unchanged Files:        {s['unchanged_files']}\n")
        f.write(f"  Modified Files:         {s['modified_files']}\n")
        f.write(f"  New Files:              {s['new_files']}\n")
        f.write(f"  Deleted Files:          {s['deleted_files']}\n")
        f.write(f"  Severity:               {s['severity']}\n")
        f.write("\n")

        if s["modified_files"] > 0:
            f.write("  Modified Files:\n")
            for file_path in report_data["details"]["modified"]:
                f.write(f"    - {file_path}\n")
            f.write("\n")

        if s["deleted_files"] > 0:
            f.write("  Deleted Files:\n")
            for file_path in report_data["details"]["deleted"]:
                f.write(f"    - {file_path}\n")
            f.write("\n")

        if s["new_files"] > 0:
            f.write("  New Files:\n")
            for file_path in report_data["details"]["new_files"]:
                f.write(f"    - {file_path}\n")
            f.write("\n")

        f.write("-" * 60 + "\n")
        f.write("  Recommended Defensive Actions\n")
        f.write("-" * 60 + "\n")
        for action in report_data["recommended_actions"]:
            f.write(f"  * {action}\n")
        f.write("\n")
        f.write("=" * 60 + "\n")
        f.write("  End of Report\n")
        f.write("=" * 60 + "\n")

    print(f"  [OK] Text report saved: {filepath}")


def save_json_report(report_data: ReportData, filepath: str) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)
    print(f"  [OK] JSON report saved: {filepath}")

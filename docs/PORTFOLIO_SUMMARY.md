# FileGuard Portfolio Summary

## Project Overview

FileGuard is a Python-based defensive cybersecurity project that monitors
file integrity using SHA-256 hashes and detects new, modified, or deleted
files. It helps verify whether important files can still be trusted.

## Why I Built It

I built this project to understand how defenders detect unauthorized file
changes. File integrity monitoring is a core skill in digital forensics and
incident response, and this project taught me how baseline comparisons work.

## Cybersecurity Concepts Learned

- **SHA-256 hashing** — cryptographically secure file fingerprinting
- **File integrity monitoring** — tracking file changes over time
- **Tamper detection** — identifying unauthorized modifications
- **Baseline comparison** — establishing known-good states
- **Digital forensics basics** — verifying data integrity and trust
- **Defensive monitoring** — proactive detection of system changes
- **Incident-style reporting** — documenting findings for response
- **Data integrity** — ensuring files have not been altered

## Technical Skills Demonstrated

- Python scripting with hashlib
- Command-line argument parsing (argparse)
- JSON data storage and retrieval
- File system traversal and hash comparison
- Severity-based risk classification
- Multi-format report generation (text + JSON)

## Portfolio Statement

> This project helped me understand that cybersecurity is also about trust
> in files and data. If important files are modified or deleted without
> authorization, defenders need a way to detect the change, investigate it,
> and respond.

## Project Links

- GitHub Repository: _(add your repo URL here)_
- Python version: 3.x (standard library only, no external dependencies)

## Screenshots

| Screenshot | Description |
|---|---|
| `screenshots/baseline-creation.png` | Running `python main.py --baseline` |
| `screenshots/integrity-check.png` | Running `python main.py --check` |
| `screenshots/generated-report.png` | Text report in `reports/integrity_report.txt` |
| `screenshots/json-report.png` | JSON report in `reports/integrity_report.json` |

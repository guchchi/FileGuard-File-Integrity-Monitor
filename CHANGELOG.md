# Changelog

## [1.0.0] — 2026-06-18

### Added

- Initial release of FileGuard
- `--baseline` command to scan `monitored_files/` and create SHA-256 hash fingerprints
- `--check` command to compare current file hashes against the saved baseline
- Detection of modified, new, and deleted files
- Severity scoring: Low (new files), Medium (single modification), High (deletions or multiple modifications)
- Terminal report output with recommended defensive actions
- Text report saved as `reports/integrity_report.txt`
- JSON report saved as `reports/integrity_report.json`
- Sample files in `monitored_files/` for testing
- Full type hints across all modules
- MIT License

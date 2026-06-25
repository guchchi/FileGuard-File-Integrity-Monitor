<div align="center">

# FileGuard — File Integrity Monitoring Tool

**SHA-256 hashing · tamper detection · baseline comparison · incident-style reporting**

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-strict-black)](https://github.com/psf/black)
[![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)](requirements.txt)

</div>

FileGuard is a defensive Python tool that monitors file integrity using SHA-256 cryptographic hashes. It detects modified, new, or deleted files by comparing current hashes against a trusted baseline, and generates actionable tamper-detection reports.

> This project was built for the **IIT Kanpur B.Cyber program** portfolio. It demonstrates defensive security thinking, file integrity monitoring, and incident-style reporting.

---

## Quick Start

```bash
git clone https://github.com/guchchi/FileGuard-File-Integrity-Monitor.git
cd FileGuard-File-Integrity-Monitor
python main.py --baseline    # Create hash baseline
python main.py --check       # Verify file integrity
```

Zero external dependencies — Python standard library only.

---

## How It Works

```
monitored_files/ → SHA-256 Baseline → Re-scan → Compare Hashes → Detect Changes → Report
```

| Step | Command | What Happens |
|---|---|---|
| 1 | `--baseline` | Scan `monitored_files/`, compute SHA-256 hashes, save to `baseline.json` |
| 2 | `--check` | Re-scan folder, compare current hashes against baseline |
| 3 | (automatic) | Classify files as unchanged, modified, new, or deleted |
| 4 | (automatic) | Assign severity and generate terminal + file reports |

---

## Detection Capabilities

| Detection | Description | Severity |
|---|---|---|
| New file added | File exists on disk but not in baseline | Low |
| File modified | Hash differs from baseline | Medium |
| File deleted | File in baseline but missing from disk | High |
| Multiple modifications | Two or more files changed | High |

---

## Usage

### Create Baseline

```bash
python main.py --baseline
```

Scans every file in `monitored_files/`, computes SHA-256 hashes, and stores them in `baseline.json`. Run this once to establish the known-good state.

### Check Integrity

```bash
python main.py --check
```

Re-scans the folder and compares each file's current hash against the baseline. Reports any changes and generates:

- `reports/integrity_report.txt` — human-readable incident report
- `reports/integrity_report.json` — structured data for automation

---

## Screenshots

| Baseline Creation | Integrity Check | Text Report | JSON Report |
|---|---|---|---|
| ![Baseline](screenshots/baseline-creation.png) | ![Check](screenshots/integrity-check.png) | ![Text](screenshots/generated-report.png) | ![JSON](screenshots/json-report.png) |

---

## Project Structure

```
FileGuard/
├── main.py                # CLI entry point
├── hasher.py              # SHA-256 hashing engine
├── monitor.py             # Baseline management and comparison
├── report.py              # Report generation (terminal, text, JSON)
├── baseline.json          # Saved hash fingerprints
├── pyproject.toml         # Package metadata
├── CHANGELOG.md           # Version history
├── LICENSE                # MIT license
├── monitored_files/       # Sample files for testing
│   ├── sample_config.txt
│   ├── user_data.txt
│   └── app_settings.txt
├── reports/               # Generated integrity reports
├── screenshots/           # README screenshots
└── docs/
    └── PORTFOLIO_SUMMARY.md
```

---

## Cybersecurity Learning Summary

File integrity monitoring is a core defensive practice. This project taught me:

- How SHA-256 provides cryptographic file fingerprinting
- Why baselines are essential for establishing trusted system state
- How tamper detection connects to digital forensics and incident response
- That structured reporting turns raw detection data into actionable intelligence

---

## License

MIT — see [LICENSE](LICENSE).

---

<div align="center">
  <sub>Built for the IIT Kanpur B.Cyber program · Defensive cybersecurity portfolio project</sub>
</div>

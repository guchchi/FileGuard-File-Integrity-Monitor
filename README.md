<div align="center">

# FileGuard — File Integrity Monitoring Tool

**SHA-256 hashing · tamper detection · baseline comparison · incident-style reporting**

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-strict-black)](https://github.com/psf/black)
[![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)](requirements.txt)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey)]()

</div>

FileGuard is a defensive Python tool that monitors file integrity using SHA-256 cryptographic hashes. It detects modified, new, or deleted files by comparing current hashes against a trusted baseline, and generates actionable tamper-detection reports. Zero external dependencies — Python standard library only.

---

## Features

- **SHA-256 cryptographic hashing** — industry-standard file fingerprinting
- **Baseline creation** — establish a known-good state of monitored files
- **Tamper detection** — detect modified, new, and deleted files
- **Severity scoring** — Low, Medium, High classification based on change type
- **Multi-format reports** — terminal output, text file, JSON
- **Recommended actions** — context-aware defensive recommendations
- **Zero dependencies** — pure Python standard library

---

## How It Works

```
monitored_files/ → SHA-256 Baseline → Re-scan → Compare Hashes → Detect Changes → Report
```

| Step | Command | What Happens |
|------|---------|--------------|
| 1 | `--baseline` | Scan `monitored_files/`, compute SHA-256 hashes, save to `baseline.json` |
| 2 | `--check` | Re-scan folder, compare current hashes against baseline |
| 3 | (automatic) | Classify files as unchanged, modified, new, or deleted |
| 4 | (automatic) | Assign severity and generate terminal + file reports |

---

## Detection Capabilities

| Detection | Description | Severity |
|-----------|-------------|----------|
| New file added | File exists on disk but not in baseline | Low |
| File modified | Hash differs from baseline | Medium |
| File deleted | File in baseline but missing from disk | High |
| Multiple modifications | Two or more files changed | High |

---

## Quick Start

```bash
git clone https://github.com/guchchi/FileGuard-File-Integrity-Monitor.git
cd FileGuard-File-Integrity-Monitor
python main.py --baseline    # Create hash baseline
python main.py --check       # Verify file integrity
```

No installation required — Python 3.8+ only.

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
    ├── PORTFOLIO_SUMMARY.md
    ├── SECURITY_REVIEW.md
    ├── INTEGRITY_LOGIC.md
    ├── THREAT_MODEL.md
    ├── EVIDENCE.md
    └── FUTURE_IMPROVEMENTS.md
```

---

## Cybersecurity Concepts Demonstrated

- **File integrity monitoring** — tracking file state over time
- **SHA-256 cryptographic hashing** — secure file fingerprinting
- **Baseline comparison** — establishing and comparing against a trusted state
- **Tamper detection** — identifying unauthorized modifications
- **Severity classification** — risk-based prioritization of findings
- **Digital forensics basics** — verifying data integrity and trust
- **Incident-style reporting** — documenting findings for response
- **Defensive monitoring** — proactive detection of system changes

---

## Ethical Disclaimer

FileGuard is a **defensive cybersecurity tool** designed for educational purposes and authorized security assessments only. It must only be used on systems you own or have explicit permission to monitor. The author is not responsible for any misuse of this tool.

---

## What I Learned

Building FileGuard taught me:

- How SHA-256 provides cryptographic file fingerprinting
- Why baselines are essential for establishing trusted system state
- How tamper detection connects to digital forensics and incident response
- That structured reporting turns raw detection data into actionable intelligence
- How severity scoring helps prioritize security findings

---

## Why File Integrity Monitoring Matters

File integrity monitoring is a core defensive practice. If an important file is changed without authorization — whether by malware, insider activity, or accidental modification — defenders need a way to detect the change, compare it with a trusted baseline, and generate evidence for investigation. FileGuard demonstrates this workflow end-to-end.

---

## Future Improvements

- Real-time file monitoring with watchdog integration
- Email or webhook alert notifications
- Encrypted baseline storage
- GUI dashboard for monitoring multiple directories
- SIEM integration with standardized output formats

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.8+ |
| Hashing | hashlib (SHA-256) |
| Storage | JSON |
| CLI | argparse |
| External deps | None |

---

## License

MIT — see [LICENSE](LICENSE).

---

<div align="center">
  <sub>Defensive cybersecurity portfolio project · File integrity monitoring · SHA-256 tamper detection</sub>
</div>

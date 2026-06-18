# FileGuard — File Integrity Monitoring Tool

FileGuard is a beginner-friendly **defensive cybersecurity project** that
monitors file integrity using SHA-256 hashes, detects file changes, and
generates tamper-detection reports.

> ⚠️ **Safety Note:** This project is **defensive and educational**. It
> monitors local sample files only. It does not attack, scan, or modify
> any external system.

---

## What This Project Demonstrates

| Skill Area | What You Learn |
|---|---|
| File Integrity Monitoring | Tracking whether files have changed |
| SHA-256 Hashing | Cryptographic file fingerprinting |
| Tamper Detection | Identifying unauthorized modifications |
| Baseline Comparison | Establishing and comparing known-good states |
| Digital Forensics Basics | Verifying data integrity and trust |
| Defensive Cybersecurity | Proactive detection of file system changes |
| Incident-style Reporting | Documenting findings for response |
| Python Scripting | hashlib, argparse, JSON, file I/O |

---

## How It Works

```
monitored_files/ → SHA-256 Baseline → Re-scan → Compare Hashes → Detect Changes → Report
```

1. **Baseline** — Scan `monitored_files/` and save SHA-256 hashes to `baseline.json`
2. **Check** — Re-scan the folder and compare current hashes against the baseline
3. **Detect** — Identify unchanged, modified, new, and deleted files
4. **Report** — Generate terminal output, text report, and JSON report

---

## Commands

### Create Baseline

```bash
python main.py --baseline
```

Scans `monitored_files/` and saves hash fingerprints to `baseline.json`.

### Check Integrity

```bash
python main.py --check
```

Compares current file hashes against the baseline and reports changes.

---

## Severity Logic

| Severity | Trigger |
|---|---|
| Low | Only new files detected |
| Medium | One modified file detected |
| High | Deleted files or multiple modified files |

---

## Sample Files

Three harmless sample files are included in `monitored_files/`:

- `sample_config.txt` — Example configuration settings
- `user_data.txt` — Example user profile data
- `app_settings.txt` — Example application configuration

These are used for testing the integrity monitoring workflow.

---

## Project Evidence & Screenshots

This section shows how FileGuard works step by step — from creating a trusted hash baseline to detecting file changes and generating reports.

---

### 1. Baseline Creation

![Baseline Creation](screenshots/baseline-creation.png)

**What this shows:**
This screenshot shows the first stage of FileGuard, where the tool scans the `monitored_files/` folder and creates a trusted baseline of SHA-256 hashes.

**Why it matters in cybersecurity:**
A baseline represents the original trusted state of files. In file integrity monitoring, this baseline is later used to detect whether a file has been modified, deleted, or newly added.

**Learning demonstrated:**

* SHA-256 hashing
* File fingerprinting
* Baseline creation
* Trusted file state recording
* Data integrity verification

---

### 2. Integrity Check

![Integrity Check](screenshots/integrity-check.png)

**What this shows:**
This screenshot shows FileGuard running an integrity check. The tool compares the current files with the saved baseline and detects changes such as modified, new, or deleted files.

**Why it matters in cybersecurity:**
Unexpected file changes can indicate accidental damage, unauthorized modification, misconfiguration, or possible tampering. File integrity monitoring helps defenders detect these changes early.

**Learning demonstrated:**

* Baseline comparison
* Tamper detection
* Modified file detection
* New file detection
* Deleted file detection
* Severity scoring

---

### 3. Generated Text Report

![Generated Report](screenshots/generated-report.png)

**What this shows:**
This screenshot shows the generated `integrity_report.txt` file. The report summarizes the scan result in a readable incident-style format.

**Why it matters in cybersecurity:**
Detection alone is not enough. Security findings must be documented clearly so they can be reviewed, investigated, and acted on. This report format connects the tool with incident response thinking.

**Learning demonstrated:**

* Incident-style reporting
* Security summary writing
* Recommended defensive actions
* Evidence-based investigation
* Clear technical documentation

---

### 4. JSON Report

![JSON Report](screenshots/json-report.png)

**What this shows:**
This screenshot shows the generated `integrity_report.json` file. The JSON report stores the scan result in a structured format.

**Why it matters in cybersecurity:**
Structured output can be used by dashboards, automation tools, monitoring systems, or future SIEM-style workflows. This makes the tool more useful beyond simple terminal output.

**Learning demonstrated:**

* Structured security reporting
* JSON-based output
* Automation-ready data
* Monitoring workflow thinking
* Defensive tool design

---

## Setup

### Prerequisites

- Python 3.6+
- No external dependencies (uses only standard library)

### Run

```bash
git clone <repo-url>
cd FileGuard
python main.py --baseline
python main.py --check
```

---

## Project Structure

```
FileGuard/
├── main.py                # Entry point (--baseline, --check)
├── hasher.py              # SHA-256 hashing engine
├── monitor.py             # Baseline management and comparison
├── report.py              # Report generator (terminal, text, JSON)
├── baseline.json          # Saved hash fingerprints
├── requirements.txt       # Dependencies (standard library only)
├── README.md              # This file
├── SECURITY.md            # Security policy
├── .gitignore
├── monitored_files/       # Sample files for monitoring
│   ├── sample_config.txt
│   ├── user_data.txt
│   └── app_settings.txt
├── reports/               # Generated integrity reports
├── screenshots/           # Screenshots for README
└── docs/
    └── PORTFOLIO_SUMMARY.md
```

---

## Cybersecurity Learning Summary

FileGuard helped me understand that cybersecurity is not only about protecting login pages or finding vulnerabilities. It is also about maintaining trust in files, configurations, and system data.

If an important file is changed without authorization, defenders need a way to detect the change, compare it with a trusted baseline, and generate evidence for investigation.

Through this project, I learned how hashing, baseline comparison, change detection, and reporting can work together in a simple defensive security workflow.

---

## Portfolio Relevance

This project supports my cybersecurity portfolio by demonstrating:

- Defensive security thinking
- File integrity monitoring and tamper detection
- Hashing and baseline comparison
- Incident-style reporting

It was built as part of my application to the **IIT Kanpur B.Cyber program**
and reflects my commitment to learning defensive cybersecurity fundamentals.

---

## License

This project is for educational and portfolio use only.

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

## Project Evidence & Screenshots

### 1. Baseline Creation

![Baseline Creation](../screenshots/baseline-creation.png)

**What this shows:**
This screenshot shows the first stage of FileGuard, where the tool scans
the `monitored_files/` folder and creates a trusted baseline of SHA-256
hashes.

**Why it matters in cybersecurity:**
A baseline represents the original trusted state of files. In file integrity
monitoring, this baseline is later used to detect whether a file has been
modified, deleted, or newly added.

**Learning demonstrated:**
SHA-256 hashing, file fingerprinting, baseline creation, trusted file state
recording, data integrity verification.

---

### 2. Integrity Check

![Integrity Check](../screenshots/integrity-check.png)

**What this shows:**
This screenshot shows FileGuard running an integrity check. The tool
compares the current files with the saved baseline and detects changes
such as modified, new, or deleted files.

**Why it matters in cybersecurity:**
Unexpected file changes can indicate accidental damage, unauthorized
modification, misconfiguration, or possible tampering. File integrity
monitoring helps defenders detect these changes early.

**Learning demonstrated:**
Baseline comparison, tamper detection, modified/new/deleted file detection,
severity scoring.

---

### 3. Generated Text Report

![Generated Report](../screenshots/generated-report.png)

**What this shows:**
This screenshot shows the generated `integrity_report.txt` file. The report
summarizes the scan result in a readable incident-style format.

**Why it matters in cybersecurity:**
Detection alone is not enough. Security findings must be documented clearly
so they can be reviewed, investigated, and acted on.

**Learning demonstrated:**
Incident-style reporting, security summary writing, recommended defensive
actions, evidence-based investigation, clear technical documentation.

---

### 4. JSON Report

![JSON Report](../screenshots/json-report.png)

**What this shows:**
This screenshot shows the generated `integrity_report.json` file. The JSON
report stores the scan result in a structured format.

**Why it matters in cybersecurity:**
Structured output can be used by dashboards, automation tools, monitoring
systems, or future SIEM-style workflows.

**Learning demonstrated:**
Structured security reporting, JSON-based output, automation-ready data,
monitoring workflow thinking, defensive tool design.

---

## Cybersecurity Learning Summary

FileGuard helped me understand that cybersecurity is not only about
protecting login pages or finding vulnerabilities. It is also about
maintaining trust in files, configurations, and system data.

If an important file is changed without authorization, defenders need a way
to detect the change, compare it with a trusted baseline, and generate
evidence for investigation.

Through this project, I learned how hashing, baseline comparison, change
detection, and reporting can work together in a simple defensive security
workflow.

## Portfolio Statement

> This project helped me understand that cybersecurity is also about trust
> in files and data. If important files are modified or deleted without
> authorization, defenders need a way to detect the change, investigate it,
> and respond.

## Project Links

- GitHub Repository: `github.com/guchchi/FileGuard-File-Integrity-Monitor`
- Python version: 3.x (standard library only, no external dependencies)

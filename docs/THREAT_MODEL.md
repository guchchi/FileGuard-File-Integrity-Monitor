# Threat Model — FileGuard

## Scope

This threat model covers FileGuard's role as a defensive file integrity
monitoring tool. It assumes FileGuard is deployed on a system where an
administrator wants to detect unauthorized file changes.

## Assets Protected

| Asset | Description |
|-------|-------------|
| Monitored files | Configuration files, data files, or any files under `monitored_files/` |
| Baseline integrity | The `baseline.json` file that stores the trusted hash reference |
| Reports | Generated integrity reports that document findings |

## Threat Actors

| Actor | Motivation | Capability |
|-------|-----------|------------|
| Casual user | Accidental modification or deletion | Low — unintentional changes |
| Insider threat | Unauthorized access or data tampering | Medium — has system access |
| Malware | File encryption, modification, or deletion | Medium-High — automated |
| External attacker | Gaining persistence, hiding evidence | High — deliberate evasion |

## Threat Scenarios

### T1: Unauthorized File Modification

**Description**: An attacker modifies a monitored configuration file to
change system behavior.

**Detection**: FileGuard detects the hash mismatch and reports the file as
"modified" with Medium severity.

**Mitigation**: Regular integrity checks catch changes between scans.

### T2: File Deletion

**Description**: An attacker deletes a monitored file to cover tracks or
disrupt operations.

**Detection**: FileGuard detects the missing file and reports it as "deleted"
with High severity.

**Mitigation**: Frequent scanning reduces the window of undetected deletion.

### T3: Rogue File Creation

**Description**: An attacker drops a malicious file into the monitored
directory.

**Detection**: FileGuard detects a file on disk that is not in the baseline
and reports it as "new" with Low severity.

**Mitigation**: Review new files to determine legitimacy.

### T4: Baseline Tampering

**Description**: An attacker modifies `baseline.json` to replace legitimate
hashes with hashes of their own malicious files.

**Detection**: By default, FileGuard does not verify the baseline's own
integrity. This is a known limitation.

**Mitigation**: Store the baseline on a separate read-only volume or sign
it with GPG. Periodically hash the baseline file and compare against a
separately stored value.

### T5: Evasion via Scan Timing

**Description**: An attacker modifies files between integrity checks and
restores them before the next scan.

**Detection**: Not detected — FileGuard only sees the current state.

**Mitigation**: Implement real-time monitoring or randomized scan intervals.

## Trust Assumptions

1. The baseline is created when the system is in a known-good state
2. The system running FileGuard is not compromised
3. The baseline file has not been tampered with
4. Files are monitored frequently enough to detect changes promptly

## Risk Summary

| Threat | Likelihood | Impact | Risk |
|--------|-----------|--------|------|
| T1: File modification | Medium | High | High |
| T2: File deletion | Low | High | Medium |
| T3: Rogue file | Medium | Low | Low |
| T4: Baseline tampering | Low | Critical | High |
| T5: Scan timing evasion | Low | Medium | Low |

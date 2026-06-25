# Integrity Logic — How FileGuard Detects Changes

## Overview

FileGuard's integrity verification is based on comparing cryptographic hash
values. Each file in the monitored directory is hashed using SHA-256, and
the resulting digest is compared against a previously recorded baseline.

## The Hash Function: SHA-256

SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function
that produces a 64-character hexadecimal digest. It has three properties
essential for integrity monitoring:

- **Deterministic**: The same input always produces the same output
- **Collision-resistant**: Finding two inputs with the same hash is
  computationally infeasible
- **One-way**: The original data cannot be derived from the hash

## Detection Logic

### Baseline Creation (`--baseline`)

```
For each file in monitored_files/:
    Read file in 64KB chunks
    Feed chunks into SHA-256 hasher
    Store {filename: hex_digest} in baseline.json
```

The 64KB chunk size balances memory usage and performance. The entire file
does not need to fit in memory — even large files can be hashed efficiently.

### Integrity Check (`--check`)

```
Load baseline.json
Re-scan monitored_files/ to get current hashes

For each file in baseline:
    If file exists and hash matches        → Unchanged
    If file exists but hash differs         → Modified (tampered)
    If file does not exist on disk          → Deleted

For each file on disk not in baseline:
    → New (unexpected file)
```

### Set Operations

FileGuard uses Python set operations for efficient comparison:

```python
common = baseline_paths & current_paths       # Files in both
deleted = baseline_paths - current_paths      # Files removed
new = current_paths - baseline_paths          # Files added
```

For files in the common set, individual hash comparison determines whether
the file was modified.

## Severity Classification

| Condition | Severity | Rationale |
|-----------|----------|-----------|
| No changes | None | System is in expected state |
| Only new files added | Low | New files may be benign |
| One file modified | Medium | Single change warrants review |
| File(s) deleted or 2+ modified | High | Indicates possible incident |

## Trust Model

FileGuard's integrity model depends on the baseline being trustworthy:

- **Before first run**: The monitored files are assumed to be in a known-good
  state
- **Baseline creation**: Trust is established at baseline time
- **Subsequent checks**: Trust is verified by comparison against the baseline

If an attacker compromises the system before the baseline is created, the
baseline itself will record the compromised state as "good." This is a
fundamental limitation of all file integrity monitoring systems — the
baseline must be created when the system is known to be clean.

# Security Review — FileGuard

## Overview

This document reviews FileGuard from a defensive cybersecurity perspective,
evaluating its approach to file integrity monitoring, cryptographic hashing,
and tamper detection.

## Strengths

### Cryptographic Hash Selection
FileGuard uses **SHA-256**, a NIST-approved cryptographic hash function with
no known practical collision attacks. It is appropriate for file integrity
verification in an educational or portfolio context.

### Baseline Integrity
The tool establishes a trusted baseline before monitoring begins. This follows
the security principle of "trust but verify" — the baseline represents the
known-good state, and all future scans compare against it.

### No External Dependencies
By using only Python's standard library (`hashlib`, `json`, `argparse`),
FileGuard minimizes its attack surface. There is no risk of supply-chain
attacks from third-party packages.

### Read-Only Monitoring
FileGuard does not modify, delete, or quarantine files. It only reads and
reports, making it safe to run on any system permitted for monitoring.

## Limitations

### Baseline Storage
The baseline is stored as plaintext JSON (`baseline.json`). An attacker who
gains write access to the baseline could replace it with hashes of their own
files, defeating detection. In a production deployment, the baseline should
be signed or stored on immutable media.

### No Real-Time Monitoring
FileGuard operates on demand (`--check`). It does not watch files
continuously. Tampering that occurs between checks will not be detected
until the next manual scan.

### No Encryption
Reports and baselines are stored in plaintext. Sensitive file paths or
metadata could be exposed if the storage location is compromised.

## Recommendations for Production Use

1. Sign the baseline file with a GPG key or store it on a read-only volume
2. Run integrity checks on a schedule (cron / Task Scheduler)
3. Encrypt reports at rest if they contain sensitive paths
4. Hash the baseline file itself to detect tampering with the baseline

## Conclusion

FileGuard is a solid demonstration of file integrity monitoring principles.
It correctly implements SHA-256 hashing, baseline comparison, and change
detection. The limitations noted are appropriate for a learning project and
can be addressed in production deployments.

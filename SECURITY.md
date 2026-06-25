# Security Policy

## Defensive & Educational Purpose

FileGuard is a **defensive cybersecurity project** built for educational
and portfolio purposes. It monitors local sample files using SHA-256
hashing to detect unauthorized changes. It does **not**:

- Attack, scan, or interact with any real systems
- Send network traffic
- Exploit vulnerabilities
- Store or transmit real credentials
- Perform any offensive action

## Intended Use

This tool is intended to help beginners learn about:

- File integrity monitoring
- SHA-256 hashing and tamper detection
- Baseline comparison for digital forensics
- Defensive monitoring and incident-style reporting

## Data Handling

FileGuard processes only files within the specified `monitored_files/`
directory. It does not:

- Read, scan, or transmit files outside the monitored directory
- Send data over any network
- Store credentials, secrets, or personal information
- Log system paths, usernames, or environment variables

Generated reports contain only filenames, hash values, and scan metadata.
No file contents are stored in baselines or reports.

## Responsible Use

This project must **only** be used:

- On your own systems
- With explicit authorization
- For educational purposes

## Reporting Concerns

If you find a security issue in this project, please open a GitHub issue.

---

_Remember: Cybersecurity is about protecting systems and data, not breaking into them._

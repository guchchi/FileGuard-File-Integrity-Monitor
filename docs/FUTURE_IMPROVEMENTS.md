# Future Improvements — FileGuard

## Short-Term Enhancements

### Real-Time File Monitoring
Integrate `watchdog` (or the native `ReadDirectoryChangesW` on Windows /
`inotify` on Linux) to detect file changes as they happen, rather than
requiring manual `--check` runs.

### Configurable Monitored Directory
Add a `--dir` argument to allow users to specify which directory to monitor,
instead of hardcoding `monitored_files/`.

### Baseline Integrity Verification
Hash the baseline file itself and store the hash separately (or sign it with
GPG). This prevents an attacker from replacing the baseline to hide their
tracks.

### Progress Indicator
Add a progress bar or percentage counter for large directories with many
files.

### Exclusion Patterns
Support `.gitignore`-style exclusion patterns so users can skip specific
files or directories (e.g., `--exclude '*.log'`).

## Medium-Term Enhancements

### Alert Notifications
Send alerts via email (SMTP), webhook (Slack/Discord), or syslog when
unauthorized changes are detected.

### Report Encryption
Encrypt generated reports using a user-provided key, so sensitive file
metadata is protected at rest.

### Multi-Directory Monitoring
Monitor multiple directories simultaneously, with separate baselines and
reporting per directory.

### Historical Tracking
Maintain a history of previous scan results to show how files have changed
over time, supporting trend analysis and forensic investigation.

### Scheduled Scanning
Built-in support for scheduling scans via cron (Linux) or Task Scheduler
(Windows) with configurable intervals.

## Long-Term Vision

### GUI Dashboard
A web-based or desktop dashboard showing real-time file status, historical
trends, and alert history. This would make the tool accessible to users who
prefer visual interfaces over command-line output.

### SIEM Integration
Output in standardized formats (CEF, LEEF, or syslog) for integration with
enterprise SIEM platforms like Splunk, Elastic Stack, or Wazuh.

### Centralized Management
A client-server architecture where multiple FileGuard instances report to a
central management server, enabling organization-wide file integrity
monitoring.

### Machine Learning Baseline
Use anomaly detection algorithms to learn normal file change patterns and
flag only truly suspicious activity, reducing false positives.

### Cross-Platform Agent
Package FileGuard as a lightweight agent for Windows, Linux, and macOS, with
automatic updates and centralized configuration management.

## Priority Matrix

| Improvement | Effort | Impact | Priority |
|-------------|--------|--------|----------|
| Configurable monitored directory | Low | High | High |
| Progress indicator | Low | Medium | Medium |
| Exclusion patterns | Low | High | High |
| Baseline integrity verification | Medium | Critical | High |
| Real-time monitoring | Medium | High | High |
| Alert notifications | Medium | High | Medium |
| Scheduled scanning | Low | High | High |
| GUI dashboard | High | Medium | Low |
| SIEM integration | High | Medium | Low |

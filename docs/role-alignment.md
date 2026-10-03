# Server security controls role alignment

This portfolio is relevant to the supplied Visa Server Security Controls job description. It demonstrates hands-on lab skills, not enterprise employment experience or deployment at Visa.

## Evidence-backed responsibilities

| Job responsibility | Project evidence | Practical limit |
| --- | --- | --- |
| Deploy, configure and maintain server security controls | Agent installation and enrollment; screenshots 26–29 | Two Ubuntu ARM64 endpoints; initial deployment settings rather than ongoing configuration enforcement |
| Monitor health and coverage | Health playbook; CSV and summary; screenshots 18 and 30–34 | Checks service and connection status; no performance monitoring or ingestion completeness assertion |
| Troubleshoot agents and infrastructure | Outage detection, Ansible recovery, subsequent healthy checks; screenshots 19–23 | Controlled service stop in a personal lab |
| Routine maintenance and version changes | Rollback and baseline restoration; screenshots 35–38 | Specific package transition, not a broad patch-management platform |
| Automation scripts and workflows | Ansible, Python and Bash source | Interactive lab execution; no scheduler or notification integration |
| Technical documentation, runbooks and reporting | Runbook, evidence index, status/version/last-keep-alive CSV and summary | Historical captures, with documented timestamp differences |
| Proof-of-concept testing and improvement | Repeat-run verification, warning simulation and version transition checks | Demonstration scope and known gaps are documented |

## Complementary detection and AI project

[Windows FIM and AI-Assisted Triage](https://github.com/thmzhanbu/wazuh-fim-ai-triage) documents file-change monitoring, custom detection rules, user/process context and a live Wazuh → Tines → Gemini triage result requiring human review. It complements agent operations by demonstrating alert handling. The repositories are cross-linked; they were not demonstrated as a single integrated deployment.

AI assistance was used during development and troubleshooting of this lab. The screenshots document the executed checks. This agent-operations project does not implement an AI/ML detection capability.

## Responsibilities outside this lab

Micro-segmentation, malware analysis, deception technology, cloud/container deployment, enterprise scale, M&A integration and ticketing workflows are not demonstrated here. The FIM project documents its own remaining tests and integration limitations. These boundaries keep interview discussion grounded in what was actually built and tested.

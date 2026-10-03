# Evidence index

The source archives were transferred from Kali and the Wazuh manager on 2026-10-03. Imported playbooks are preserved; only reporting file-path handling was adjusted for repository portability.

## Included reporting snapshots

- agents.json: enrolled agent list.
- agent-001.json / agent-002.json: individual manager records.
- coverage.csv: historical status/version/last-keep-alive report.
- summary.txt: historical PASS summary with UTC generation time.

The imported JSON and CSV last-keep-alive values differ, so these are separate historical snapshots rather than an atomic evidence set.

## Included screenshots

39 PNG screenshots were copied from the supplied Desktop/wazuh folder, with their original names and pixels preserved. These capture lab setup and test results; numbering is retained even where earlier proposed names differed.

| Group | What the captures document |
| --- | --- |
| 01–06 (including 01a) | VM resources, baseline, clean snapshot, installation completion, services and dashboard |
| 07–14 | First endpoint baseline, connectivity, enrollment, disconnection and recovery |
| 15–23 | SSH/Ansible access, health checks, outage detection and automated service recovery |
| 24–29 | Second endpoint access, deployment, enrollment, repeat deployment and manager status |
| 30–34 | CSV reporting, refreshed data, PASS, simulated warning and restoration |
| 35–38 | Package rollback health, manager verification, restored version and service health |

The warning in screenshot 33 is a simulation using edited CSV data, not a live service outage. Screenshot 36 shows the manager observing agent version 4.14.7 as Active; screenshot 37 shows restored 4.14.8 as Active/PASS, and screenshot 38 shows installed package 4.14.8-1 with a passing service health check. Snapshot creation is documented; snapshot restoration was not demonstrated.

### Screenshot links

- [01-vm-resources.png](../evidence/screenshots/01-vm-resources.png)
- [01a-vm-resources.png](../evidence/screenshots/01a-vm-resources.png)
- [02-server-baseline.png](../evidence/screenshots/02-server-baseline.png)
- [03-clean-snapshot.png](../evidence/screenshots/03-clean-snapshot.png)
- [04-wazuh-installation.png](../evidence/screenshots/04-wazuh-installation.png)
- [05-wazuh-services.png](../evidence/screenshots/05-wazuh-services.png)
- [06-wazuh-dashboard.png](../evidence/screenshots/06-wazuh-dashboard.png)
- [07-linux-agent-01-baseline.png](../evidence/screenshots/07-linux-agent-01-baseline.png)
- [08-agent-manager-connectivity.png](../evidence/screenshots/08-agent-manager-connectivity.png)
- [09-static-ip-connectivity.png](../evidence/screenshots/09-static-ip-connectivity.png)
- [10-linux-agent-service.png](../evidence/screenshots/10-linux-agent-service.png)
- [11-linux-agent-enrolled.png](../evidence/screenshots/11-linux-agent-enrolled.png)
- [12-linux-agent-inventory.png](../evidence/screenshots/12-linux-agent-inventory.png)
- [13-agent-disconnected.png](../evidence/screenshots/13-agent-disconnected.png)
- [14-agent-recovered.png](../evidence/screenshots/14-agent-recovered.png)
- [15-ssh-access.png](../evidence/screenshots/15-ssh-access.png)
- [16-ansible-connectivity.png](../evidence/screenshots/16-ansible-connectivity.png)
- [17-ansible-sudo-access.png](../evidence/screenshots/17-ansible-sudo-access.png)
- [18-ansible-health-check.png](../evidence/screenshots/18-ansible-health-check.png)
- [19-health-check-detects-outage.png](../evidence/screenshots/19-health-check-detects-outage.png)
- [20-health-check-recovered.png](../evidence/screenshots/20-health-check-recovered.png)
- [21-ansible-agent-recovery.png](../evidence/screenshots/21-ansible-agent-recovery.png)
- [22-recovery-verification.png](../evidence/screenshots/22-recovery-verification.png)
- [23-automated-recovery-dashboard.png](../evidence/screenshots/23-automated-recovery-dashboard.png)
- [24-agent02-ansible-connectivity.png](../evidence/screenshots/24-agent02-ansible-connectivity.png)
- [25-agent02-sudo-access.png](../evidence/screenshots/25-agent02-sudo-access.png)
- [26-ansible-agent-deployment.png](../evidence/screenshots/26-ansible-agent-deployment.png)
- [27-agent02-enrolled.png](../evidence/screenshots/27-agent02-enrolled.png)
- [28-agent02-deployment-verification.png](../evidence/screenshots/28-agent02-deployment-verification.png)
- [29-manager-agent-status.png](../evidence/screenshots/29-manager-agent-status.png)
- [30-coverage-report.png](../evidence/screenshots/30-coverage-report.png)
- [31-refreshed-coverage-report.png](../evidence/screenshots/31-refreshed-coverage-report.png)
- [32-coverage-summary-pass.png](../evidence/screenshots/32-coverage-summary-pass.png)
- [33-coverage-summary-warning.png](../evidence/screenshots/33-coverage-summary-warning.png)
- [34-coverage-summary-restored.png](../evidence/screenshots/34-coverage-summary-restored.png)
- [35-package-rollback-health.png](../evidence/screenshots/35-package-rollback-health.png)
- [36-rollback-manager-verification.png](../evidence/screenshots/36-rollback-manager-verification.png)
- [37-restored-version-manager.png](../evidence/screenshots/37-restored-version-manager.png)
- [38-restored-version-health.png](../evidence/screenshots/38-restored-version-health.png)

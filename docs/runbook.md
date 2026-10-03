# Operating runbook

## Before changes

Confirm endpoint IPs, SSH access and sudo access. Keep the Wazuh server running. Take a snapshot of the endpoint before package maintenance. Save the installed package version and manager version. The manager must be the same version or newer than the agent. The rollback playbook targets agent-02 using its inventory; do not run it against an unintended group.

## Kali: connectivity and deployment

Run from `ansible/`:

```bash
ansible -i inventory-agent02.ini linux_agents -m ping -k
ansible -i inventory-agent02.ini linux_agents -m command -a whoami -b -k -K
ansible-playbook -i inventory-agent02.ini deploy-agent.yml --syntax-check
ansible-playbook -i inventory-agent02.ini deploy-agent.yml -k -K
ansible-playbook -i inventory-agent02.ini health-check.yml -k -K
```

Expect pong, root, a successful install, and active service. Confirm enrollment/Active on the manager. Repeat deployment should report zero changes when already at the desired version and service state. Ad hoc command modules may say CHANGED for read-only commands; that is not evidence of a system mutation.

## Service recovery

For an authorized lab outage, stop `wazuh-agent` on the test endpoint. Run the health playbook and record its failed assertion. Run `ensure-agent.yml`, then health-check again; verify manager connectivity. Repeat ensure-agent and expect zero changes. Use `inventory.ini` for agent-01 and `inventory-agent02.ini` for agent-02.

## Package rollback and restoration

Run from `ansible/`, after taking the endpoint snapshot:

```bash
ansible-playbook -i inventory-agent02.ini rollback-agent.yml --syntax-check
ansible-playbook -i inventory-agent02.ini rollback-agent.yml -k -K
ansible -i inventory-agent02.ini linux_agents -m command -a "dpkg-query -W wazuh-agent" -k
ansible-playbook -i inventory-agent02.ini health-check.yml -k -K
```

Accept 4.14.7-1, active service and manager Active/v4.14.7. Restore with deploy-agent.yml; repeat the package and health checks and require 4.14.8-1 and manager Active/v4.14.8. If package installation or connectivity fails, inspect logs and retain the snapshot as recovery contingency. Snapshot restoration may revert endpoint configuration and keys; validate SSH address and manager connectivity afterward.

## Manager: reporting

Run from the copied `reporting/` directory:

```bash
bash collect-report.sh
```

Outputs: agents.json, agent-001.json, agent-002.json, coverage.csv and summary.txt. Require ID 002 Active/PASS. ID 001 is planned offline in this lab. The `ip: any` field is an enrollment address constraint, not the endpoint's current network IP.

The repository scripts use their own directory for files; this differs from the original VM scripts' home-directory paths. Run them on the manager to collect live data. Imported evidence remains in a separate directory.

## Summary warning test

Use a scratch copy of the report and summary script. Change ID 002 from Active to Disconnected in the CSV, run summary.py and require ATTENTION REQUIRED. Remove ID 002's CSV row to exercise Missing. These are input simulations. Restore live inputs by rerunning the collector; require Active/PASS.

## Troubleshooting

- SSH refused: check SSH service and IP on the destination VM.
- SSH no hostkeys: generate host keys with sudo ssh-keygen -A, then restart SSH.
- No hosts matched: the group is linux_agents (underscore).
- YAML parsing error: preserve indentation; apt options must align under the module.
- Paste escape at the start of YAML: remove the control sequence and rerun syntax-check.
- Service active but manager disconnected: collect fresh manager status, then inspect endpoint `/var/ossec/logs/ossec.log` and network reachability if it persists.

## Publication

Review files and screenshots for secrets and unrelated personal content. Publish source files and selected evidence, not VM images or installer credential archives. Record tested versions and preserve the distinction between observed lab outcomes and untested production behavior.

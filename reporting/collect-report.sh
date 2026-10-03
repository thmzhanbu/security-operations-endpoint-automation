#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
sudo /var/ossec/bin/agent_control -l -j > agents.json
sudo /var/ossec/bin/agent_control -i 001 -j > agent-001.json
sudo /var/ossec/bin/agent_control -i 002 -j > agent-002.json
python3 report.py
python3 summary.py

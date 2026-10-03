import csv
from pathlib import Path
from datetime import datetime, timezone

folder = Path(__file__).resolve().parent

with (folder / "coverage.csv").open() as source:
    agents = {row["id"]: row for row in csv.DictReader(source)}

agent = agents.get("002")
status = agent["status"] if agent else "Missing"

text = "\n".join([
    "Report generated UTC: " + datetime.now(timezone.utc).isoformat(),
    "Planned offline: 001 (lab memory limits)",
    "Expected online: 002",
    "Agent 002 status: " + status,
    "Result: " + ("PASS" if status == "Active" else "ATTENTION REQUIRED"),
]) + "\n"

(folder / "summary.txt").write_text(text)

print(text)

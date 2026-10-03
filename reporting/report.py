import csv
import json
from pathlib import Path
from datetime import datetime, timezone

folder = Path(__file__).parent
notes = {
     "001": "Intentionally powered off for lab memory limits",
     "002": "Expected online",
}

with (folder / "coverage.csv").open("w", newline="") as output:
    writer = csv.writer(output)
    writer.writerow(["id", "name", "status", "version", "last_keep_alive_utc", "note"])
    for agent_id in ("001", "002"):
        result = json.loads((folder / f"agent-{agent_id}.json").read_text())
        if result ["error"] != 0:
            raise RuntimeError(result)
        agent = result["data"]
        timestamp = int(agent["lastKeepAlive"])
        last_seen = datetime.fromtimestamp(timestamp, timezone.utc).isoformat()
        writer.writerow([
            agent["id"],
            agent["name"],
            agent["status"],
            agent["version"],
            last_seen,
            notes[agent_id],
        ])

print((folder / "coverage.csv").read_text())

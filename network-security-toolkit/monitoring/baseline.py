import subprocess
import json
import psutil
import datetime

def capture_baseline(output_file: str = "baseline.json") -> dict:
    """Captures current network state and saves to file."""
    result = subprocess.run(["netstat", "-an", "-p", "tcp"], capture_output=True, text=True)
    connections = []
    for line in result.stdout.splitlines():
        if "LISTEN" in line or "ESTABLISHED" in line:
            connections.append(line.strip())

    interfaces = {}
    for iface, addrs in psutil.net_if_addrs().items():
        interfaces[iface] = [addr.address for addr in addrs]

    baseline = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "connections": connections,
        "interfaces": interfaces
    }

    with open(output_file, "w") as f:
        json.dump(baseline, f, indent=2)

    return baseline



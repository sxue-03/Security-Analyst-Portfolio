import re
import pandas as pd
from collections import Counter

LOG_FILE = "sample_logs.txt"
OUTPUT_FILE = "alerts.csv"

def parse_logs(file_path):
    pattern = re.compile(r'Failed password.*from ([\d.]+)')
    ip_counts = Counter()

    with open(file_path, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ip_counts[match.group(1)] += 1
    return ip_counts

def detect_bruteforce(ip_counts, threshold=3):
    alerts = []
    for ip, count in ip_counts.items():
        if count >= threshold:
            alerts.append({"IP": ip, "Attempts": count, "Alert": "Possible Brute Force"})
    return alerts

def save_to_csv(alerts, filename):
    if not alerts:
        print("No alerts detected.")
        return
    df = pd.DataFrame(alerts)
    df.to_csv(filename, index=False)
    print(f"Alerts saved to {filename}")

if __name__ == "__main__":
    print("Analyzing logs...")
    ip_counts = parse_logs(LOG_FILE)
    alerts = detect_bruteforce(ip_counts)
    save_to_csv(alerts, OUTPUT_FILE)

import json
def load_rules(filename="rules.json"):
    with open(filename) as f:
        return json.load(f)
rules = load_rules()
DANGEROUS_PORTS = [22, 23, 3306, 5432, 3389, 6379, 27017]
PORT_NAMES = {
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    3389: "RDP",
    6379: "Redis",
    27017: "MongoDB"
}
def analyze_rule(rule):
    port = rule["port"]
    source = rule["source"]
    if source == "0.0.0.0/0" and port in DANGEROUS_PORTS:
        return "DANGER"
    elif source == "0.0.0.0/0" and port not in DANGEROUS_PORTS:
        return "WARNING"
    else:
        return "SAFE"
for rule in rules:
    label = analyze_rule(rule)
    port_name = PORT_NAMES.get(rule["port"], "Unknown")
    print(f"[{label}] Rule {rule['rule_id']} - Port {rule['port']} ({port_name}) from {rule['source']}")

labels = [analyze_rule(rule) for rule in rules]

print("\n--- Summary ---")
print(f"DANGER  : {labels.count('DANGER')}")
print(f"WARNING : {labels.count('WARNING')}")
print(f"SAFE    : {labels.count('SAFE')}")
print(f"Total   : {len(rules)}")

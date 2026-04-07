import boto3
def audit_firewall(region: str = "us-east-1") -> dict:
    """Audits AWS Security Groups for risky inbound rules."""
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_security_groups()
    groups = response["SecurityGroups"] 
    risky_ports = [22, 3389, 3306, 5432, 27017, 6379]  # SSH, RDP, MySQL, Postgres, MongoDB, Redis
    risky_rules = []
    for sg in groups:
        for rule in sg["IpPermissions"]:
            port = rule.get("FromPort")
            for ip_range in rule.get("IpRanges", []):
                if ip_range["CidrIp"] == "0.0.0.0/0" and port in risky_ports:
                    risky_rules.append({
                        "group_id": sg["GroupId"],
                        "group_name": sg["GroupName"],
                        "port": port,
                        "cidr": ip_range["CidrIp"]
                    })
    findings = []
    for rule in risky_rules:
        findings.append(f"Port {rule['port']} open to {rule['cidr']} on {rule['group_id']} ({rule['group_name']})")

    return {
        "region": region,
        "security_groups_checked": len(groups),
        "risky_rules": risky_rules,
        "findings": findings
}


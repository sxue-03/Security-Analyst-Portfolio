import dns.resolver
def check_dns(domain: str) -> dict:
    """Returns DNS security findings for a domain."""
    # Stage 1 - SPF
    spf_record = None
    txt_records = dns.resolver.resolve(domain, 'TXT')
    for record in txt_records:
        txt = record.to_text().strip('"')
        if txt.startswith("v=spf1"):
            spf_record = txt
            break
    dmarc_record = None
    dmarc_records = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
    for record in dmarc_records:
        txt = record.to_text().strip('"')
        if txt.startswith("v=DMARC1"):
            dmarc_record = txt
            break
    dnssec_enabled = False
    try:
        dns.resolver.resolve(domain, 'DNSKEY')
        dnssec_enabled = True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        dnssec_enabled = False
    findings = []

    if not spf_record:
        findings.append("No SPF record found")
    if not dmarc_record:
        findings.append("No DMARC record found")
    if not dnssec_enabled:
        findings.append("DNSSEC not enabled")

    return {
        "domain": domain,
        "spf": spf_record,
        "dmarc": dmarc_record,
        "dnssec_enabled": dnssec_enabled,
        "findings": findings
    }




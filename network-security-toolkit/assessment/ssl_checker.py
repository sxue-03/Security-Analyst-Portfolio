import ssl
import socket
from datetime import datetime, timezone
def check_ssl(host: str, port: int = 443) -> dict:
    """Returns findings for a single host."""
    context = ssl.create_default_context()
    with socket.create_connection((host, port), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
    expire_date = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
    weak_keywords = ["RC4", "DES", "3DES", "NULL", "EXPORT", "anon"]
    cipher_name = cipher[0]
    weak_ciphers = [kw for kw in weak_keywords if kw in cipher_name]
    self_signed = cert["issuer"] == cert["subject"]
    now = datetime.now(timezone.utc)
    days_left = (expire_date - now).days
    findings = []
    if days_left < 30:
        findings.append(f"Certificate expiring soon: {days_left} days left")
    if days_left < 0:
        findings.append("Certificate is expired")
    if weak_ciphers:
        findings.append(f"Weak ciphers detected: {weak_ciphers}")
    if self_signed:
        findings.append("Certificate is self-signed")
    return {
        "host": host,
        "port": port,
        "expired": days_left < 0,
        "days_until_expiry": days_left,
        "self_signed": self_signed,
        "weak_ciphers": weak_ciphers,
        "cipher": cipher_name,
        "findings": findings
    }



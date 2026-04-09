# Network Security Project — Firewall Rule Analyzer

## What I Learned

### What is a Firewall?
A firewall controls what traffic is allowed in and out of a network. It works like a security guard at the door — it checks every request coming in and decides whether to allow it or block it based on rules.

### What are IP Addresses?
An IP address identifies a specific device on a network. There are two types:
- **Private IP** — used inside a network (e.g. 192.168.1.5 or 10.0.0.1). Not accessible from the internet directly.
- **Public IP** — used on the internet. This is what the outside world sees.

**NAT (Network Address Translation)** is what converts a private IP to a public IP when traffic leaves the network to go to the internet.

### What is CIDR (the /number)?
CIDR notation tells you how large a network range is. The number after the `/` shows how many IP addresses are included.

| CIDR | Meaning |
|------|---------|
| `0.0.0.0/0` | Everyone — the entire internet |
| `10.0.0.0/8` | All internal IPs starting with 10.x.x.x |
| `192.168.1.0/24` | A small local network (254 devices) |
| `192.168.1.5/32` | One specific device only |

### What are Ports?
A port identifies which service on a device you are trying to reach. Think of an IP address as a building and a port as the specific door inside that building.

| Port | Service | Risk if open to internet |
|------|---------|--------------------------|
| 22 | SSH (remote terminal) | HIGH — should be restricted |
| 80 | HTTP (web, unencrypted) | LOW — okay for public websites |
| 443 | HTTPS (web, encrypted) | LOW — okay for public websites |
| 3306 | MySQL (database) | CRITICAL — never open to internet |
| 5432 | PostgreSQL (database) | CRITICAL — never open to internet |
| 3389 | RDP (Windows remote desktop) | CRITICAL — never open to internet |
| 6379 | Redis (cache) | CRITICAL — never open to internet |

### The Most Dangerous Firewall Rule
```
ALLOW ALL from 0.0.0.0/0 to ANY
```
This means: let everyone on the internet reach everything. This is a critical misconfiguration.

---

## What I Built

A Python script that reads a set of firewall rules and analyzes each one for security risks. It labels every rule as **DANGER**, **WARNING**, or **SAFE** based on what port is exposed and who can reach it.

### How it works
- Loads firewall rules from `rules.json`
- Checks if a sensitive port is open to `0.0.0.0/0` (the whole internet)
- Labels each rule and prints a summary

### Risk Labels
| Label | Meaning |
|-------|---------|
| DANGER | Sensitive port (SSH, RDP, database) open to the entire internet |
| WARNING | Non-sensitive port open to the entire internet |
| SAFE | Access is restricted to a specific IP or internal network |

---

## How to Run

```bash
cd network-security-project
python3 firewall_analyzer.py
```

## Sample Output

```
[DANGER]  Rule 1 - Port 22 (SSH) from 0.0.0.0/0
[WARNING] Rule 2 - Port 443 (HTTPS) from 0.0.0.0/0
[DANGER]  Rule 3 - Port 3306 (MySQL) from 0.0.0.0/0
[WARNING] Rule 4 - Port 80 (HTTP) from 0.0.0.0/0
[SAFE]    Rule 5 - Port 22 (SSH) from 10.0.0.0/8
[DANGER]  Rule 6 - Port 3389 (RDP) from 0.0.0.0/0
[SAFE]    Rule 7 - Port 443 (HTTPS) from 192.168.1.5/32

--- Summary ---
DANGER  : 3
WARNING : 2
SAFE    : 2
Total   : 7
```

## Purpose

This project demonstrates how a security analyst reviews firewall rules to identify misconfigurations. In a real environment, rules like "SSH open to 0.0.0.0/0" or "MySQL open to the internet" are critical findings that need to be fixed immediately.

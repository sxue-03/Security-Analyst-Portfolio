# IAM Access Auditor

A Python script that automates user access reviews by reading a CSV export of user accounts and flagging risky accounts for security review.

## Problem

When employees join a company they get accounts and access. When they leave or change roles, that access often doesn't get cleaned up. Ghost accounts, unused admin privileges, and disabled-but-still-active accounts are common entry points for attackers. Security teams typically review these manually — this script automates that process.

## What it does

Reads a `users.csv` file and flags accounts that need review:

- **Inactive (90+ days)** — user hasn't logged in recently
- **Never logged in** — account exists but was never used
- **Disabled accounts** — account is disabled but still present in the system
- **Admin review** — user has elevated privileges and requires regular review

## Sample output

```
===== IAM AUDIT REPORT =====
Total users: 6
Flagged accounts: 5
INACTIVE (90+ days): ['jsmith', 'mgarcia']
NEVER LOGGED IN: ['bwilson']
DISABLED ACCOUNTS: ['tjones']
ADMIN REVIEW: ['mgarcia', 'rchen']
```

## How to run it

```
python3 auditor.py
```

Requires Python 3. No external libraries needed.

## What I learned

The goal of this project is not just coding or building the final result. It’s about going through the process, understanding how things work, and learning the logic behind each step.

## Tools used

- Python 3
- `csv` module
- `datetime` module

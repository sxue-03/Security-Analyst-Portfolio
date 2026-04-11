import json
import sys
import os
from datetime import datetime
ROLE_PERMISSIONS = {
    "engineer": ["Google", "Hubspot", "Github"],
    "it":  ['Google', "Hubspot", "Zoom: basic license"],
    "sale": ["Google",'Hubspot','Zoom: business license']
}
def load_payload(path):
    with open(path) as f:
        return json.load(f)
def onboard(payload):
    role = payload['role']
    full_name = payload["full_name"]
    start_date = payload['start_date']
    permissions = ROLE_PERMISSIONS[role]
    print("=== Onboarding Profile ===")
    print(f"Name: {full_name}")
    print(f"Role: {role}")
    print(f"Start Date: {start_date}")
    print(f"Please enable {full_name}'s access: ")
    for perm in permissions:
        print(f"{perm}")
if __name__ == "__main__": 
    path = sys.argv[1]
    data = load_payload(path)
    onboard(data)



import requests
api_key = 'YOUR_API_KEY_HERE'
ip = input('enter ip to check:')
url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
respone = requests.get(url, headers={'x-apikey': api_key})
data = respone.json()
stats = data['data']['attributes']['last_analysis_stats']
print(f"IP: {ip} | Malicious: {stats['malicious']} | Harmless: {stats['harmless']}")

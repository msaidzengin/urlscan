import requests
import json
import time

url = 'https://urlscan.io/api/v1/search/?q=domain:'
words = ["banka", "devlet", "korona"]
results = []

for word in words:
    r = requests.get(url + word)
    if r.status_code == 200:
        data = r.json()
        results += data['results']
        print(word + " sonuc sayisi: " + str(len(data['results'])))
        time.sleep(2)

with open('results.json', 'w') as f:
    json.dump(results, f)
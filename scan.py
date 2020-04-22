import requests
import json
import time

url = 'https://urlscan.io/api/v1/search/?q='
words = ["banka", "devlet", "korona"]
results = {}
result_list = []

for word in words:
    r = requests.get(url + word)
    if r.status_code == 200:
        data = r.json()
        results[word] = data['results']
        result_list += data['results']
        print(word + " | sonuc sayisi: " + str(len(data['results'])))
        time.sleep(2)

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("result.json kaydedildi.")
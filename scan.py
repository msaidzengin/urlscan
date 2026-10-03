import json
import time

import requests

SEARCH_URL = "https://urlscan.io/api/v1/search/?q="
KEYWORDS = ["banka", "devlet", "korona"]
OUTPUT_PATH = "result.json"


def main():
    result_url_list = {}

    for word in KEYWORDS:
        response = requests.get(SEARCH_URL + word)
        if response.status_code != 200:
            continue

        data = response.json()
        result_url_list[word] = [item["task"]["url"] for item in data["results"]]
        print(f"{word} | sonuc sayisi: {len(data['results'])}")
        time.sleep(2)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as output_file:
        json.dump(result_url_list, output_file, ensure_ascii=False, indent=4)

    print("result.json kaydedildi.")


if __name__ == "__main__":
    main()

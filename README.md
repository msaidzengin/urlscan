# urlscan

A small Python script that queries the public urlscan.io search API for the keywords `banka`, `devlet`, and `korona`, then writes the matching page URLs to `result.json`.

Written on 22 April 2020 and last updated on 23 April 2020.

## Run

```bash
pip install -r requirements.txt
python3 scan.py
```

Successful searches pause for two seconds. The script prints how many results each keyword returned, then saves `result.json` in the current directory. That file is generated output and is not kept in the repository.

# check_urls_existence.py
import os
import sys
import requests

def check_url_existence(url, api_key, search_engine_id):
    search_url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={url}"
    response = requests.get(search_url)
    search_results = response.json()
    return "items" in search_results

if __name__ == "__main__":
    api_key = os.environ["GOOGLE_API_KEY"]
    search_engine_id = os.environ["GOOGLE_SEARCH_ENGINE_ID"]
    url = sys.argv[1]
    exists = check_url_existence(url, api_key, search_engine_id)
    print(f"{url} exists: {exists}")

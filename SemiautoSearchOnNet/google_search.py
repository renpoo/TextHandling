# google_search.py
import requests

def google_search(query, api_key, search_engine_id):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": search_engine_id,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Request failed with status code {response.status_code}")

if __name__ == '__main__':
    import sys
    query = sys.argv[1]
    api_key = sys.argv[2]
    search_engine_id = sys.argv[3]
    search_results = google_search(query, api_key, search_engine_id)
    print(search_results)

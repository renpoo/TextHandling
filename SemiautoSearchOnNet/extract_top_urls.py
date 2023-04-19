# extract_top_urls.py
from logger import log_to_file

@log_to_file('extract_top_urls_log.txt')
def extract_top_urls(search_results, top_n=3):
    urls = []
    for item in search_results.get('items', []):
        urls.append(item['link'])
        if len(urls) >= top_n:
            break

    print(urls)

    return urls

if __name__ == '__main__':
    import json
    import sys

    search_results_json = sys.argv[1]
    top_n = int(sys.argv[2])

    with open(search_results_json, "r") as f:
        search_results = json.load(f)

    top_urls = extract_top_urls(search_results, top_n)
    print("\n".join(top_urls))

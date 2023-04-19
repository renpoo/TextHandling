# get_search_results.py
import sys
import os
from google_search import google_search
from extract_top_urls import extract_top_urls
from logger import log_to_file

@log_to_file('get_search_results_log.txt')
def get_search_results(title_authors, args):
    search_results = []

    for title, authors in title_authors:
        query = f"{title} {authors}"
        results = google_search(query, args.api_key, args.search_engine_id)
        top_urls = extract_top_urls(results, top_n=3)
        search_results.append((title, authors, top_urls))

    print(search_results)

    return search_results


if __name__ == '__main__':
    title_authors = sys.argv[1]
    args = sys.argv[2]

    get_search_results(title_authors, args)
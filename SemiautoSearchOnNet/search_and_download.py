# search_and_download.py
import os
import sys
from extract_urls import extract_urls_from_file
from check_urls_existence import check_url_existence
from download_files import download_file
from open_urls_in_safari import open_url_in_safari

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_folder = sys.argv[2]

    api_key = os.environ["GOOGLE_API_KEY"]
    search_engine_id = os.environ["GOOGLE_SEARCH_ENGINE_ID"]

    urls = extract_urls_from_file(input_file)

    for url in urls:
        exists = check_url_existence(url, api_key, search_engine_id)
        if exists:
            download_file(url, output_folder)
#            open_url_in_safari(url)

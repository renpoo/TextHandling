# downloader_with_search.py
import os
import argparse
from extract_top_urls import extract_top_urls
from get_search_results import get_search_results
from parse_input_file import parse_input_file
from save_search_results import save_search_results
from download_pdfs import download_pdfs_from_list

def main(args):
    title_authors = parse_input_file(args.input_file)
    search_results = get_search_results(title_authors, args)
    save_search_results(search_results, args.search_output_file)
    download_pdfs_from_list(args.search_output_file, args.output_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Semi-automatic Literature Search and Download")
    parser.add_argument("input_file", help="Input file containing book titles and authors")
    parser.add_argument("output_folder", help="Output folder for PDFs")
    parser.add_argument("search_output_file", help="Search output file containing top-3 URL candidates")
    parser.add_argument("--api_key", required=True, help="Google Custom Search API Key")
    parser.add_argument("--search_engine_id", required=True, help="Google Custom Search Engine ID")

    args = parser.parse_args()

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    main(args)


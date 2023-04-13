# open_urls_in_safari.py
import os
import sys

def open_url_in_safari(url):
    os.system(f"open -a Safari {url}")

if __name__ == "__main__":
    url = sys.argv[1]
    open_url_in_safari(url)

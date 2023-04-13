# extract_urls.py
import re
import sys

def extract_urls_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    url_pattern = re.compile(r"https?://\S+")
    urls = url_pattern.findall(content)
    return urls

if __name__ == "__main__":
    file_path = sys.argv[1]
    urls = extract_urls_from_file(file_path)
    for url in urls:
        print(url)

# download_files.py
import os
import sys
import requests

def download_file(url, output_folder):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    if not file_name.endswith((".pdf", ".html")):
        file_name += ".html"
    output_path = os.path.join(output_folder, file_name)
    with open(output_path, "wb") as file:
        file.write(response.content)

if __name__ == "__main__":
    url = sys.argv[1]
    output_folder = sys.argv[2]
    os.makedirs(output_folder, exist_ok=True)
    download_file(url, output_folder)

# download_pdfs.py
import os
import sys
import time
import string
import subprocess
from urllib.parse import unquote
from logger import log_to_file

def sanitize_url(url):
    safe_characters = string.ascii_letters + string.digits + "-_."
    decoded_url = unquote(url)
    sanitized_url = ''.join(c if c in safe_characters else '_' for c in decoded_url)
    return sanitized_url

def download_pdfs_from_list(search_output_file, output_folder):
    with open(search_output_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        title, authors, urls = line.strip().split("\t")
        for url in urls.split(", "):
            save_url_as_pdf(url, title, authors, output_folder)

def save_url_as_pdf_using_wkhtmltopdf(url, pdf_path):
    cmd = ["wkhtmltopdf", url, pdf_path]
    result = subprocess.run(cmd, capture_output=True)
    return result.stdout.decode("utf-8")


@log_to_file('save_url_as_pdf_log.txt')
def save_url_as_pdf(url, title, authors, output_folder):
    # Prepare the PDF file name
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
    sanitized_url = sanitize_url(url)
    file_name = f"{sanitized_url}-{timestamp}.pdf"
    pdf_path = os.path.join(output_folder, file_name)

    # Try to download the PDF file
    try:
        if url.lower().endswith(".pdf"):
            # Download directly if the URL is a PDF file
            print("##### Downloading PDF directly...")
            print("##### From: ", url)
            print("##### To: ", pdf_path)
            subprocess.run(["curl", "-L", "-o", pdf_path, url], check=True)
        else:
            # Save the web page as a PDF using Safari
            print("##### Save the web page as a PDF...")
            print("##### From: ", url)
            print("##### To: ", pdf_path)
            save_url_as_pdf_using_wkhtmltopdf(url, pdf_path)

        print(f"Successfully saved '{pdf_path}'")
    except Exception as e:
        print(f"Failed to save '{file_name}': {e}")

if __name__ == '__main__':
    search_output_file = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    download_pdfs_from_list(search_output_file, output_folder)





# # download_pdfs.py
# import os
# import subprocess
# import time
# from run_applescript import run_applescript

# def save_url_as_pdf(url, title, authors, output_folder):
#     # Prepare the PDF file name
#     timestamp = time.strftime('%Y-%m-%d %H-%M-%S')
#     file_name = f"{title} - {authors} - {timestamp}.pdf"
#     pdf_path = os.path.join(output_folder, file_name)

#     # Try to download the PDF file
#     try:
#         if url.lower().endswith(".pdf"):
#             # Download directly if the URL is a PDF file
#             try:
#                 subprocess.run(["curl", "-L", "-o", pdf_path, url], check=True)
#             except subprocess.CalledProcessError as e:
#                 raise Exception(f"curl error: {e}")
#         else:
#             # Save the web page as a PDF using Safari's "Save as PDF" feature
#             applescript = f"""
#             on saveUrlAsPdf(url, outputPdfPath)
#                 tell application "Safari"
#                     activate
#                     make new document with properties {{URL:url}}
#                     delay 5
#                 end tell

#                 set theFile to outputPdfPath

#                 tell application "System Events"
#                     tell process "Safari"
#                         set frontmost to true
#                         keystroke "p" using command down
#                         delay 1
#                         keystroke "p" using {{command down, option down}}
#                         delay 1
#                         set value of text field 1 of sheet 1 of window 1 to theFile
#                         delay 1
#                         click button "Save" of sheet 1 of window 1
#                         delay 1
#                     end tell
#                 end tell

#                 tell application "Safari"
#                     close the front document
#                 end tell
#                 return theFile
#             end saveUrlAsPdf

#             saveUrlAsPdf("{url}", "{pdf_path}")
#             """
#             run_applescript(applescript)

#         print(f"Successfully saved '{file_name}'")
#     except Exception as e:
#         print(f"Failed to save '{file_name}': {e}")

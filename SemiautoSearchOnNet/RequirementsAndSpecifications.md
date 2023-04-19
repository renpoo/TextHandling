# Semi-automatic Literature Search and Download

## Requirements

1. Parse an input text file containing book titles and authors in the format "Title: ******\nAuthor(s): ******".
2. For each title and author(s) pair, perform a Google search using the Google Custom Search API.
3. Extract the top-3 URL candidates from the search results.
4. Save the top-3 URL candidates adding to a combined text file, one list for each title and author(s) pair.
5. Download the webpage of each URL candidate as a PDF file, according to the combined URLs list file.
6. The Download methods are "Download directly the target .pdf file" or "Save the web page as .pdf via Safari Browser, for each web page, a tab opened".
7. Save each PDF file in a specified output folder with the file name format "Title - Author(s) - (date & timestamp).pdf".
8. Save intermediate results (for every steps) in separate text files to log for debugging purposes.

## Specifications

- The main script should be able to run with a single command specifying the input file, output folder for PDFs, and an optional search output file.
- Each function should be designed to be used independently.
- The input text file should have one title and author(s) pair per line, separated by a tab character.
- The Google Custom Search API should be used for performing the search.
- The output folder should be created if it does not exist.
- If a search output file is specified, it should contain a long list of the top-3 URL candidates for each title and author(s) pair.
- The PDF file should be saved in the output folder with the file name format "Title - Author(s) - (date & timestamp).pdf".
- Intermediate results should be saved in separate text files for debugging purposes.

## Restrictions

1. Every script should have a header containing the script's filename as a comment.

## Scripts

1. `parse_input_file.py`
2. `google_search.py`
3. `extract_top_urls.py`
4. `save_search_results.py`
5. `download_pdfs.py`
6. `run_applescript.py`
7. `downloader_with_search.py`

## Functions

1. `parse_input_file(input_file)` in `parse_input_file.py`
2. `google_search(query, api_key, search_engine_id)` in `google_search.py`
3. `extract_top_urls(search_results, top_n)` in `extract_top_urls.py`
4. `save_search_results(title_authors, search_results, search_output_file)` in `save_search_results.py`
5. `download_pdfs_from_list(search_output_file, output_folder)` in `download_pdfs.py`
6. `save_url_as_pdf(url, title, authors, output_folder)` in `download_pdfs.py`
7. `run_applescript(*args)` in `run_applescript.py`
8. `main(input_file, output_folder, search_output_file)` in `downloader_with_search.py`

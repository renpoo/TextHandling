# Semi-automatic Literature Search and Download

This project is designed to semi-automatically search for literature based on book titles and authors, and then download the top search results as PDF files. The project uses the Google Custom Search API to perform searches and retrieve relevant URLs, either downloading the PDF directly or saving the web page as a PDF using Safari.

## Requirements

- Python 3.6 or higher
- Google Custom Search API Key
- Google Custom Search Engine ID

## Installation

1. Clone this repository:
```sh
git clone https://github.com/your_username/semi-automatic-literature-search.git
```

2. Install the required Python packages:
```sh
pip install -r requirements.txt
```

## Usage

1. Prepare an input text file containing book titles and authors in the following format, with one title and author(s) pair per line separated by a tab character:

```txt
Title: Book Title 1
Author(s): Author(s) 1
Title: Book Title 2
Author(s): Author(s) 2
...
```

2. Set your Google Custom Search API key and Search Engine ID as environment variables:
```sh
export GOOGLE_API_KEY="your_api_key"
export GOOGLE_SEARCH_ENGINE_ID="your_search_engine_id"
```

3. Run the main script:
```sh
python downloader_with_search.py input_file.txt output_folder [search_output_file]
```

- `input_file.txt`: The input text file containing book titles and authors.
- `output_folder`: The folder where the downloaded PDFs will be saved.
- `search_output_file` (optional): A file to save the search results, including the top-3 URL candidates for each title and author(s) pair.

## Troubleshooting

- If you encounter any issues, check the log files generated in the project folder. These files contain intermediate results and can help you identify any problems.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


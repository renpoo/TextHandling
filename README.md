# TextHandling
## Scraping PDFs from the internet and summarizing their contents as .txt files

This project contains two main functionalities:

1. **SemiautoSearchOnNet**: Search for and download documents (PDF or HTML files that can be printed as PDFs) from the internet using an input .txt file.
2. **TextSummaries**: Extract text from PDF files, preprocess the text, summarize it, and perform postprocessing on the summarized text using a combination of Automator & "Text > Summarize" with some shell scripts and Python code (by executing Automator.workflow on macOS).

## SemiautoSearchOnNet

To search for and download documents, use the `search_and_download.py` script with the following command:

```sh
python search_and_download.py input_file output_folder
```

Before using the Google Search API, you need to define the following shell environment variables:

Google Search via API (maybe defined in .zshrc):
```sh
export GOOGLE_API_KEY="XXXXXX"
export GOOGLE_SEARCH_ENGINE_ID="YYYYYY"
```

## TextSummaries

For the downloaded .pdf files, you can summarize their contents using the TextSummaries workflow.

1. Place the PDF files you want to process in the `PdfsToSummarize` folder.
2. Run the main Automator.workflow.
3. The summarized text will be generated in the `PostprocessedSummarizedTexts` folder.


Good luck with your text handling journey!
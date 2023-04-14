# Text Summarization Workflow

This project contains a set of scripts and an Automator workflow to extract text from PDF files, preprocess the text, summarize it, and perform postprocessing on the summarized text.

## Requirements

1. Extract text from PDF files.
2. Preprocess the extracted text:
    - Remove unnecessary spaces.
    - Remove escape characters.
    - Separate Japanese and English text.
3. Summarize the preprocessed text.
4. Postprocess the summarized text:
    - Replace single spaces with newlines.
5. Organize the output into separate folders.

## Specifications

1. Use the Automator tool on macOS.
2. Organize the process into separate child workflows for modularity and better management.
3. Implement Python scripts for text preprocessing, summarization, and postprocessing.
4. Folders used in the process:
    - PdfsToSummarize: Contains input PDF files.
    - TextsFromPdfs: Contains extracted text from PDF files.
    - PreprocessedTexts: Contains preprocessed text.
    - SummarizedTexts: Contains summarized text.
    - PostprocessedSummarizedTexts: Contains postprocessed summarized text.

## Setup

1. Clone this repository.
2. Install required Python packages using `pip install -r requirements.txt`.
3. Make sure the Automator workflows are properly set up and configured.

## Usage

1. Place the PDF files you want to process in the `PdfsToSummarize` folder.
2. Run the main Automator workflow.
3. The summarized text will be generated in the `PostprocessedSummarizedTexts` folder.

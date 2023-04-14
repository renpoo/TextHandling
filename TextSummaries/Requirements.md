### Requirements

1. **Root Automator.workflow**
   - Calls child Automator workflows for each step in the process.

2. **pdf_to_text.workflow**
   - Extracts text from PDF files in the folder "PdfsToSummarize".
   - Saves extracted text as .txt files in the folder "TextsFromPdfs".

3. **text_preprocessing.workflow**
   - Calls text_preprocessing.py with input and output folder paths.
   - Preprocesses the extracted text:
     1. Removes special characters.
     2. Replaces multiple spaces with a single space.
     3. Removes unnecessary line breaks.
   - Saves the preprocessed text in the folder "PreprocessedTexts".

4. **text_summarization.workflow**
   - Uses macOS's built-in "Text > Summarize" feature in Automator.
   - Optionally, sets the summary size.
   - Saves the summarized text in the folder "SummarizedTexts".

5. **text_postprocessing.workflow**
   - Calls text_postprocessing.py with input and output folder paths.
   - Replaces single space with a new line character in the summarized text.
   - Saves the postprocessed text in the folder "PostprocessedSummarizedTexts".

6. **Python scripts**
   - `text_preprocessing.py` for text preprocessing.
   - `text_postprocessing.py` for text postprocessing.

7. **Shell scripts**
   - For passing arguments and calling Python scripts within Automator workflows.
   - For handling file and folder paths.

8. **Folder structure**
   - PdfsToSummarize: for input PDF files.
   - TextsFromPdfs: for extracted text files.
   - PreprocessedTexts: for preprocessed text files.
   - SummarizedTexts: for summarized text files.
   - PostprocessedSummarizedTexts: for postprocessed summarized text files.

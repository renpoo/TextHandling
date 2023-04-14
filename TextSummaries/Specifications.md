### Specifications

1. **Root Automator.workflow**
   - Calls the following child Automator workflows in order:
     1. pdf_to_text.workflow
     2. text_preprocessing.workflow
     3. text_summarization.workflow
     4. text_postprocessing.workflow

2. **pdf_to_text.workflow**
   - Uses `pdftotext` to convert PDF files in the "PdfsToSummarize" folder to .txt files.
   - Saves the .txt files in the "TextsFromPdfs" folder.

3. **text_preprocessing.workflow**
   - Calls `text_preprocessing.py` with the "TextsFromPdfs" folder as input and the "PreprocessedTexts" folder as output.
   - The Python script processes each .txt file, removing special characters, multiple spaces, and unnecessary line breaks.

4. **text_summarization.workflow**
   - Utilizes the macOS "Text > Summarize" Automator action.
   - Allows setting of the summary size (optional).
   - Summarizes the preprocessed text files in the "PreprocessedTexts" folder.
   - Saves the summarized text files in the "SummarizedTexts" folder.

5. **text_postprocessing.workflow**
   - Calls `text_postprocessing.py` with the "SummarizedTexts" folder as input and the "PostprocessedSummarizedTexts" folder as output.
   - The Python script processes each summarized .txt file, replacing single spaces with new line characters.

6. **Python scripts**
   - `text_preprocessing.py`: Takes input and output folder paths as arguments and processes .txt files accordingly.
   - `text_postprocessing.py`: Takes input and output folder paths as arguments and processes .txt files accordingly.

7. **Shell scripts**
   - Used to pass arguments and call Python scripts within Automator workflows.
   - Handles file and folder paths in a compatible way with zsh.

8. **Folder structure**
   - PdfsToSummarize: Input folder for PDF files.
   - TextsFromPdfs: Output folder for extracted .txt files.
   - PreprocessedTexts: Output folder for preprocessed .txt files.
   - SummarizedTexts: Output folder for summarized .txt files.
   - PostprocessedSummarizedTexts: Output folder for postprocessed summarized .txt files.

import os
import re
import sys

def preprocess_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove unnecessary escape characters
    text = text.replace('\\', '')

    # Replace multiple newlines with a single space
    text = re.sub(r'\n+', ' ', text)

    # # Delete unnecessary newlines
    # text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

    # # Replace multiple spaces with a single space
    # text = re.sub(r' +', ' ', text)

    # Replace two or more spaces with a single space
    text = re.sub(r' {2,}', ' ', text)

    # Separate chapters or paragraphs
    text = re.sub(r'([\u3000]+)', r'\n\1\n', text)
    text = re.sub(r'([a-zA-Z]\.)\n', r'\1', text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    preprocess_text(input_file, output_file)

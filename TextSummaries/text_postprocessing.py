import os
import re
import sys

def postprocess_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace single spaces with new lines
    text = text.replace(' ', '\n')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    postprocess_text(input_file, output_file)

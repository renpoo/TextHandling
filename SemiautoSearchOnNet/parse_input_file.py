# parse_input_file.py
from logger import log_to_file

@log_to_file('parse_input_file_log.txt')
def parse_input_file(input_file):
    title_authors = []
    with open(input_file, 'r') as file:
        for line in file:
            if line.startswith("Title:"):
                title = line.strip().split("Title:")[1].strip()
            elif line.startswith("Author(s):"):
                authors = line.strip().split("Author(s):")[1].strip()
                title_authors.append((title, authors))

    for title, authors in title_authors:
        print(f"Title: {title}\nAuthor(s): {authors}\n")

    return title_authors

if __name__ == '__main__':
    import sys
    input_file = sys.argv[1]
    title_authors = parse_input_file(input_file)


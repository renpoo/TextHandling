# save_search_results.py
from logger import log_to_file

@log_to_file('save_search_results_log.txt')
def save_search_results(search_results, search_output_file):
    print(search_results)

    with open(search_output_file, 'a') as output_file:
        for title, authors, urls in search_results:
            output_file.write(f"{title}\t{authors}\t{', '.join(urls)}\n")

if __name__ == '__main__':
    import sys

    title_authors_file = sys.argv[1]
    search_results_file = sys.argv[2]
    output_file = sys.argv[3]

    with open(title_authors_file, "r") as f:
        title_authors = [tuple(line.strip().split("\t")) for line in f.readlines()]

    with open(search_results_file, "r") as f:
        search_results = [line.strip().split(", ") for line in f.readlines()]

    save_search_results(title_authors, search_results, output_file)

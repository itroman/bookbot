from stats import num_words, num_chars, sorted_chars
from reports import reporting
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def sys_argv_check():
    try:
        filepath = sys.argv[1]
    except IndexError as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    sys_argv_check()
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    word_count = num_words(contents)
    chars = num_chars(contents)
    reporting(filepath, word_count)
    return sorted_chars(chars)

main()
import sys

from stats import get_num_words, get_enum_carac, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    num_words = get_num_words(book_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    enum_carac = get_enum_carac(book_contents)
    print("--------- Character Count -------")
    for el in sort_dict(enum_carac):
        if el["char"].isalpha():
            print(f"{el["char"]}: {el["num"]}")
    print("============= END ===============")


main()
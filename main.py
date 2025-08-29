import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_word_count(text)
        char_count = get_character_count(text)
        stats = sort_stats(char_count)
        bookpath_report = f"Analyzing book found at {book_path}..."
        words_report = f"Found {num_words} total words"


        print ("============ BOOKBOT ============")
        print (bookpath_report)
        print ("----------- Word Count ----------")
        print (words_report)
        print ("--------- Character Count -------")
        for entry in stats:
            if entry["char"].isalpha():
                print(f"{entry['char']}: {entry['num']}")
        print ("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import sort_stats
from stats import get_character_count
from stats import get_word_count
main()
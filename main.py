from stats import get_word_count
from stats import get_char_count
from stats import organize_list
import sys

# returns the text of the book as a string
def get_book_text(book):
    return book.read()

def main():
    # stores inputed book as a variable
    with open(sys.argv[1]) as book:
        # returns the text of the book as a string
        book_text = get_book_text(book)

        # returns how many words there are in the book as an int
        word_count = get_word_count(book_text)

        # returns how many of each char is in the book as a dict
        char_count = get_char_count(book_text)

        # organizes and returns char_count as a list of dicts
        my_list = organize_list(char_count)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book.name}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        # prints each char there is in the book and how many
        for each in my_list:
            if each["char"].isalpha():
                print(f"{each["char"]}: {each["num"]}")
        print("============= END ===============")

# checks if there was 1 argument passed with the script and if not exits and print error message
count = 0
for each in sys.argv:
    count +=1
if count != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()

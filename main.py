from stats import get_word_count
from stats import get_char_count
from stats import organize_list
import sys

def get_book_text(book):
    return book.read()

def main():
    with open(sys.argv[1]) as book:
        book_text = get_book_text(book)
        #print(book_text)

        word_count = get_word_count(book_text)
        #print(f"{word_count} words found in the document")

        char_count = get_char_count(book_text)
        #print(char_count)

        my_list = organize_list(char_count)
        #print(my_list)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book.name}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for each in my_list:
            if each["char"].isalpha():
                print(f"{each["char"]}: {each["num"]}")
        print("============= END ===============")

count = 0
for each in sys.argv:
    count +=1
if count != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()

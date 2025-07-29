def get_word_count(book):
    split_book = book.split()
    word_count = 0
    for each in split_book:
        word_count += 1
    return word_count

def get_char_count(text):
    new_text = text.lower()
    char_list = list(new_text)
    char_count = {}
    for char in char_list:
        found = False
        for each in char_count:
            if each == char:
                found = True
        if found:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count

def organize_list(my_dict):

    my_list = []

    for each in my_dict:
        my_list.append({"char": each, "num": my_dict.get(each)})

    def sort_on(item):
        return item["char"]

    my_list.sort(key=sort_on)
    
    return my_list


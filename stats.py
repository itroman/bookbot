def num_words(book_contents):
    words = book_contents.split()
    number = len(words)
    return number

def num_chars(book_contents):
    char_dict = {}
    lowered_book_contents = book_contents.lower()
    chars = list(lowered_book_contents)
    for char in chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(chars):
    return chars["count"]

def sorted_chars(char_dict):
    list = []
    for dict in char_dict:
        count = char_dict[dict]
        list.append({"char": dict, "count": count})
    list.sort(reverse=True, key=sort_on)
    for i in range(0, len(list)):
        if (list[i]['char']).isalpha():
            print(f"{list[i]['char']}: {list[i]['count']}")


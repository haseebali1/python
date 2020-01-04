# Common Words

def find_word_in_file(filename, word_to_find):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        return contents.lower().count(word_to_find)

print("The number of times \"the\" appears in a word in the book is " +
        str(find_word_in_file('files/book.txt', 'the')))
print("The number of times \"the\" appears in the book is " +
        str(find_word_in_file('files/book.txt', 'the ')))


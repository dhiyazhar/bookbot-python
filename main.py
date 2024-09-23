import string

def open_book():
    with open('books/frankenstein.txt', 'r', encoding="utf-8") as f:
        read_book = f.read()
    
    return read_book
        
def word_count(book):
    word_count = len(book.split())

    return word_count

def character_count(book):
    alphabet_list = string.ascii_lowercase
    
    for x in alphabet_list:
        temp = book.count(x)
        print(f"The {x} character was found {temp} times")

def main():
    book = open_book()
    
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{word_count(book)} words found in the document")
    print(" ")
    print(character_count(book))
    print("--- End report ---")

if __name__ == '__main__':
    main()
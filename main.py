def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()

    words = word_count(file_contents)
    chars = char_count(file_contents)

    report(words,chars, book_path)


def word_count(text:str) -> int:
    split_words = text.split()
    print(len(split_words))
    return len(split_words)

def char_count(text:str):
    letter_count = {}
    for letter in text.lower():
        letter_count[letter] = letter_count.get(letter, 0) + 1
        
    return letter_count

def report(word_count:int,char_count:dict, book):
    print(f'Begin report of {book}')
    print(f'{word_count} words found in the document.')
    for char, count in sorted(char_count.items()):
        if char.isalpha():
            print(f'{char} was counted {count} times')
    print('End report')

main()
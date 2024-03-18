
def main():
    book_path = "books/frankenstein.txt"
    text = pull_book_text(book_path)
    print(text)
    report(text)
    #sort_on()

def pull_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count
def count_letters(text):
    chars = {}
    count = 0
    string = text
    lowered_string = text.lower()
    for char in lowered_string:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1 
    sorted_char = dict(sorted(chars.items(), key=lambda x: x[1], reverse=True))
    return sorted_char
def report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    chars_dict = count_letters(text)
    for char, count in chars_dict.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
    

           
    
main()

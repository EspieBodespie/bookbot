def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict = count_chars(text)
    book_report(book_path, word_count, char_dict)
    
    
def book_report(book_path, word_count, char_dict):
    sorted_chars = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    print(f"Book report for '{book_path}")
    print(f"There are {word_count} words in this book")
    for char, count in sorted_chars:
        print(f"{char} appears {count} times")
    print("END REPORT")





# Reads File at <path>
def get_book_text(path):
    with open(path) as f:
        return f.read()


# Counts the words in file
def count_words(string):
    return len(string.split())

 
# Create dict of character counts a-z
def count_chars(string):
    chars = {}
    lower_str = string.lower()
    for char in lower_str:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars




main()

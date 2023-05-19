def main():
    book_path = 'books/frankenstein.txt'
    text = read_book(book_path)
    num_words = count_words(text)
    num_letters = count_letters(text)
    sorted_list = sort_letters(num_letters)
    my_report= generate_report(book_path, text, num_words, sorted_list)
    print(my_report)

def read_book(path):
    with open(path) as f:
        return f.read()
        
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    result = {}
    for keys in text:
        result[keys] = result.get(keys, 0) + 1
    return result

def sort_letters(my_dict):
    filtered_dict = {k: v for k, v in my_dict.items() if k.isalpha()}
    sorted_list = sorted(filtered_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_list

def generate_report(book_path, text, num_words, sorted_list):
    report = f"--- Begin report of {book_path} ---\n"
    report += f"{num_words} words found in the document\n\n"

    for item in sorted_list:
        report += f"The '{item[0]}' character was found {item[1]} times\n"

    report += "--- End report ---"
    return report

main()
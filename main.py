def count_words(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_letters(book):
    letters_count = dict()
    for l in book:
        if l.lower() in letters_count:
            letters_count[l.lower()] += 1
        else:
            letters_count[l.lower()] = 1

    return letters_count

def sort_on(d):
    return d["num"]

def get_report(book_path,text,num_words,num_letters_dict):
    sorted_dl = []
    for x in num_letters_dict:
        if x.isalpha():
            sorted_dl.append({"letter": f"{x}", "num": num_letters_dict[x]})
    sorted_dl.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---\n\
    {num_words} words found in the document\n")
    for i in sorted_dl:
        print(f"The '{i["letter"]}' character was found {i["num"]} times")
    print("--- End report ---")
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_letters_dict = get_count_letters(text)
    get_report(book_path,text,num_words,num_letters_dict)
main()
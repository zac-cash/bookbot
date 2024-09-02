path_to_file = './books/frankenstein.txt'

def main():
    bookcontents = Get_Text(path_to_file)
    w_count = Word_Count(bookcontents)
    char_count = Char_Count(bookcontents)

    print(f"Sup. Welcome to the book report. We are working on the file: {path_to_file}\n")
    print(f"There are {w_count} words in the book.")
    print("The following is a count of each letter in the book:")
    print(char_count)

def Word_Count (string):
    return len(string.split())

def Char_Count (string):
    returning_dict = {}
    for char in string.lower():
        if char not in returning_dict:
            returning_dict[char] = 1
        else:
            returning_dict[char] += 1
    return returning_dict

def Get_Text (filepath):
        with open(path_to_file) as f:
            filecontents = f.read()
        return filecontents
main()
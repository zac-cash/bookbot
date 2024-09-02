path_to_file = './books/frankenstein.txt'

def main():
    bookcontents = Get_Text(path_to_file)
    char_list_of_dict = Create_Char_List(Char_Count(bookcontents))

    print(f"Sup. Welcome to the book report. \nWe are working on the file: {path_to_file.split('/')[-1]}\n")
    print(f"There are {Word_Count(Get_Text(path_to_file))} words in the book.")
    
    print("The following is a count of each letter in the book:")
    for char_dict in char_list_of_dict:
        if char_dict['char'].isalpha():
            print(f"The '{char_dict['char']}' was found {char_dict['num']} times.")
    print("--- End Book report ---")

def Get_Text (filepath):
    with open(path_to_file) as f:
        return f.read()

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

def Create_Char_List (dict):
    list_of_char = []
    for key in dict:
        list_of_char.append(
            {
                "char": key,
                "num": dict[key]
            })
    list_of_char.sort(reverse=True,key=sort_on)
    return list_of_char

def sort_on(dict):
    return dict["num"]
main()
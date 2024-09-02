path_to_file = './books/frankenstein.txt'

def Word_Count (string):
    return len(string.split())

def main():
    with open(path_to_file) as f:
        filecontents = f.read()
    w_count = Word_Count(filecontents)
    print(f"there are {w_count} words in frankenstein.txt")

main()
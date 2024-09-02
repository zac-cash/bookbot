path_to_file = './books/frankenstein.txt'

def main():
    with open(path_to_file) as f:
        filecontents = f.read()
    print(filecontents)

main()
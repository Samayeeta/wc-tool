import sys
import argparse

def count_bytes(file):
    content = file.read()  
    bytes_count = len(content.encode('utf-8')) 
    print(bytes_count)

def count_lines(file):
    content = file.readlines()  
    print(len(content))

def count_words(file):
    content = file.read()  
    words = content.split()  
    print(len(words))

def count_chars(file):
    content = file.read()  
    print(len(content)) 

def count_all(file):
    content = file.read() 
    lines = content.splitlines() 
    words = content.split()
    bytes_count = len(content.encode('utf-8'))  
    print(len(lines), len(words), bytes_count)

def main():
    parser = argparse.ArgumentParser(description="A simple version of the wc tool to count lines, words, characters, or bytes in a file.")
    parser.add_argument('file', nargs='?', type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin, help="The file to process - if not provided, reads from standard input.")
    parser.add_argument('-c', action='store_true', help="Count bytes")
    parser.add_argument('-l', action='store_true', help="Count lines")
    parser.add_argument('-w', action='store_true', help="Count words")
    parser.add_argument('-m', action='store_true', help="Count characters")

    args = parser.parse_args()

    file = args.file

    if args.c:
        count_bytes(file)
    elif args.l:
        count_lines(file)
    elif args.w:
        count_words(file)
    elif args.m:
        count_chars(file)
    else:
        count_all(file)

if __name__ == "__main__":
    main()
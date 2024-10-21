import sys

def count_bytes():
    with open("test.txt", "r", encoding="utf-8") as file:  # Open in text mode
        content = file.read()  # Read the file as text
        bytes_count = len(content.encode('utf-8'))  # Convert text to bytes
        print(bytes_count)

def count_lines():
    with open("test.txt", "r", encoding="utf-8") as file:  # Open in text mode
        content = file.readlines()  # Read all the lines
        print(len(content))  # Count lines

def count_words():
    with open("test.txt", "r", encoding="utf-8") as file:  # Open in text mode
        content = file.read()  # Read all the text
        words = content.split()  # Split the text into words
        print(len(words))  # Count words

def count_chars():
    with open("test.txt", "r", encoding="utf-8") as file:  # Open in text mode
        content = file.read()  # Read all the text
        print(len(content))  # Count characters

def count_all():
    with open("test.txt", "r", encoding="utf-8") as file:  # Open in text mode
        content = file.read()  # Read all the text
        lines = content.splitlines()  # Split the text by lines
        words = content.split()  # Split the text by words
        bytes_count = len(content.encode('utf-8'))  # Convert text to bytes
        print(len(lines), len(words), bytes_count)  # Print lines, words, bytes

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "-c":
            count_bytes()
        elif sys.argv[1] == "-l":
            count_lines()
        elif sys.argv[1] == "-w":
            count_words()
        elif sys.argv[1] == "-m":
            count_chars()
    else:
        count_all()
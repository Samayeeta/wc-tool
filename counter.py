import sys

def count_bytes():
    with open("test.txt", "r", encoding="utf-8") as file: 
        content = file.read() 
        bytes_count = len(content.encode('utf-8')) 
        print(bytes_count)

def count_lines():
    with open("test.txt", "r", encoding="utf-8") as file:  
        content = file.readlines()  
        print(len(content))  

def count_words():
    with open("test.txt", "r", encoding="utf-8") as file:  
        content = file.read()  
        words = content.split()  
        print(len(words))  

def count_chars():
    with open("test.txt", "r", encoding="utf-8") as file: 
        content = file.read()  
        print(len(content))  

def count_all():
    with open("test.txt", "r", encoding="utf-8") as file: 
        content = file.read()  
        lines = content.splitlines()
        words = content.split()  
        bytes_count = len(content.encode('utf-8'))  
        print(len(lines), len(words), bytes_count) 

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
"""
Connor Cox
U4 Lab 2
Reversal
"""
from StackClass import ArrayStack

def get_content():
    path = "earnest.txt"
    with open(path, 'r') as file:
        contents = file.readlines()
    
    return contents

def clean(contents):
    cleaned = ""
    for i, line in enumerate(contents):
        line = list(line)
        for i, char in enumerate(line):
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or ord(char) == 32:
                cleaned += char
            else:
                del line[i]
    
    return cleaned

def reverse(text):
    original = text.split(" ")
    stack = ArrayStack()
    for word in original:
        stack.push(word)
    
    new = ""
    for i in range(len(stack)):
        new += stack.pop()
        if i < len(stack):
            new += " "
    
    return new

def write_out(reversed):
    path = "reversed.txt"
    with open(path, 'w') as file:
        file.write(reversed)

def main():
    contents = get_content()
    cleaned = clean(contents)
    reversed = reverse(cleaned)
    write_out(reversed)


if __name__ == "__main__":
    main()
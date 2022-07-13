
import re


def is_valid(char_index):
    pattern = re.compile('\d\d?')
    return pattern.match(char_index)


print("Welcome to char finder")
index = input("Please provide character index: ")

if is_valid(index):
    word = input("Good. Now give me the nice long word: ")
    if int(index) <= len(word):
        symbol = word[int(index)]
        char_finder = f"The symbol #{index} in \"{word}\" is \"{symbol}\"."
        print(char_finder)
    else:
        print("Error. Index is out of range")
else:
    print("Error. Index should be a whole positive number")











import string

def is_pangram(sentence):
    letters = set(sentence.lower())
    return set(string.ascii_lowercase).issubset(letters)

s = input("Enter sentence: ")

if is_pangram(s):
    print("Pangram")
else:
    print("Not a Pangram")
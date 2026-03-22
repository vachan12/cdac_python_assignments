def is_palindrome_phrase(sentence):
    
    cleaned = ""
    
    # remove punctuation and spaces
    for ch in sentence.lower():
        if ch.isalpha():
            cleaned += ch
    
    # check palindrome
    return cleaned == cleaned[::-1]


s = input("Enter a sentence: ")

if is_palindrome_phrase(s):
    print("Palindrome phrase")
else:
    print("Not a palindrome")
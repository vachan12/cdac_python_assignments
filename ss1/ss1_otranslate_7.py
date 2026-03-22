def translate(text):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in text:
        if ch.isalpha() and ch not in vowels:
            result += ch + "o" + ch
        else:
            result += ch

    return result

text="this is fun"

res=translate(text)
print(res)
def longest_word(lst,n):
    res_words=[word for word in lst if len(word)>n ]
    return len(res_words[0])

lst=["My name is vachan","hi","kate","kite","kit kat"]

res=longest_word(lst,7)
print(res)
    
def longest_word(lst,n):
    res_words=[word for word in lst if len(word)>n ]
    return res_words

lst=["My name is vachan","hi","kate","kite","kit kat"]

res=longest_word(lst,7)
print(res)
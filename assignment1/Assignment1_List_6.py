lst=['Ashish','','Satyarth','','Satyarth','Ashish','','Ashish']
for i in lst:
    if i=='':
        lst.remove('')
print(lst)
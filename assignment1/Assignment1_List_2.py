list1=[]
list2=[]
print('Enter 5 numbers for list1: ')
for i in range(5):
    list1.append(str(input()))
print('Enter 5 numbers for list2: ')
for i in range(5):
    list2.append(str(input()))
reslist=[]
for i in range(5):
    reslist.append(list1[i]+list2[i])
print('The resultant list is ',reslist)
pri
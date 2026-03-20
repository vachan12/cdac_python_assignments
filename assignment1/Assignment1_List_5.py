list1=[];list2=[]
n1=int(input('Enter number of elements in list1: '))
for i in range(n1):
    list1.append(int(input()))
n2=int(input('Enter number of elements in list2: '))
for i in range(n2):
    list2.append(int(input()))
for i in range(len(list1)):
    print(list1[i],' ',list2[n1-1-i])    
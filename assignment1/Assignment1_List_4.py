list1=[]
lis2=[]
n1=int(input('Enter number of elements in list1: '))
for i in range(n1):
    list1.append(str(input()))
n2=int(input('Enter number of elements in list2: '))
for i in range(n2):
    lis2.append(str(input()))
reslist=[]
for i in range(len(list1)):
    for j in range(len(lis2)):
        reslist.append(list1[i]+lis2[j])
print(reslist)
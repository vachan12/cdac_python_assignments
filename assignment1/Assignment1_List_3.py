import math
lst=[]
lst2=[]

for i in range(5):
    n=int(input())
    lst.append(n)
    lst2.append(math.pow(n,2))
print(lst2)
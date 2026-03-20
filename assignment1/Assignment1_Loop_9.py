import math
x=int(input('Enter the value of x: '))
n=int(input('Enter number of terms: '))
d=1;sum=0
for i in range(n):
    if i!=0:
        d=d*i
    sum=sum+((math.pow(x,i))/d)
    print(sum)
    print(d)
print('The sum of the series is ',sum)
import math
x=int(input('Enter the value of x: '))
n=int(input('Enter number of terms: '))
flag=0
sum=0
cnt=1
num=0
for i in range(n):
    if i%2==0:
        num=math.pow(x,cnt)
        sum=sum+num
    else:
        num=-(math.pow(x,cnt))
        sum=sum+num
    print(num)
    cnt=cnt+2
print('The sum of the series is ',sum)
n=int(input("Enter the value of n"))
sum=0;cnt=0
while n>0:
    sum=sum+(n%10)
    cnt=cnt+1
    n=n//10
print('The sum of digits is ',sum)
print('No of digits are: ',cnt)
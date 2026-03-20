print('Enter 20 numbers:')
sum=0
for i in range(20):
    n=int(input())
    if n%2==0:
        sum=sum+n
print('The sum of even numbers is ',sum)
n=input('Enter numbers: ')
p=1;sum=0;cnt=0
while str(n)!='q':
    sum=sum+int(n)
    p=p*int(n)
    cnt=cnt+1
    n=input()
print('The average is ',sum/cnt)
print('The product is ',p)
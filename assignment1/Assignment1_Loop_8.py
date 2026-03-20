import math
# n=int(input("Enter the value of n "))
# nine_sum=0
# next_nine=0
# total=0
# for i in range(n):
#     nine_sum=next_nine+9
#     total+=nine_sum
#     next_nine=nine_sum*10
# print('The sum of the series is ',total)

n=int(input("Enter the value of n"))
sum=0
for i in range(1,n+1):
    sum=sum+(math.pow(10,i)-1)
print('The sum of the series is ',sum)


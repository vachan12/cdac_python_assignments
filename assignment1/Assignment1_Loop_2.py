'''for i in range(4):
    j=0
    while j<=i:
        print('*',end=' ')
        j=j+1
    print()'''


# a
# print("Enter the value of n")
# n=int(input())
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# c
# print("Enter the value of n(odd)")
# n=int(input())
# l=0
# for i in range(n,0,-2):
#     for k in range(l):
#         print(' ',end=' ')
#     for j in range(i):
#         if(j%2==0):
#             print('1',end=' ')
#         else:
#             print('0',end=' ')
#     l=l+1
#     print()

n=int(input("Enter the value of n"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=' ')
    print()
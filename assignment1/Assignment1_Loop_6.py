#cube calculator
import math
n=int(input("Enter the value of n"))

for i in range(1,n):
    print(f"The cube of {i} is {math.pow(i,3)}")
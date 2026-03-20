
m=int(input("Enter the value of m"))
n=int(input("Enter the value of n"))

less= m if m<n  else n
for i in range(1,less+1):
    if m%i==0 and n%i==0:
        hcf=i
print("The HCF of ",m," and ",n," is ",hcf)
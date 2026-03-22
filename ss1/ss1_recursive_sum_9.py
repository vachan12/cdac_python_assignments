#recursive sum

x=int(input("Enter x: "))

def sum(n):
    if n == 1:
        return 1
    else:
        return n+sum(n-1)

s=sum(x)
print(f"recursive sum is:{s}")

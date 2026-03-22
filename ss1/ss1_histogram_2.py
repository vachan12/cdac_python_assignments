#histogram

int_list=[]
choice=0
while choice!=-1:
    choice=int(input("Enter the integer or -1 to quit:"))
    if(choice != -1):
        int_list.append(choice)
for i in int_list:
    print("*"*i,end="")
    print()

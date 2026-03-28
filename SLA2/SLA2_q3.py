#Menu driven

choice=0
lst=[]

while choice !=9:
    choice=int(input("""
                     1. Accept Data 
                        a) add at last position 
                        b) add at given position 
                    2. Delete data by value 
                    display message deleted successfully  
                    or not found 
                    3. delete data by position 
                        a) delete last element 
                        b) delete from particular position 
                    4. sort  
                        a) ascending  
                        b) descending 
                    5. reverse 
                    6. Print in sorted order without changing original list 
                    7. print in reverse order without changing original list 
                    8. display data 
                        a) normal  
                        b) numbered 
                    9.Exit

                     Enter your choice: 
                     """))
                     
    match choice:
        case 1:
            sub_ch=input("Enter sub choice(a or b): ")
            if sub_ch.lower() == "a":
                data=input("Enter Data: ")
                lst.append(data)
                print("{data} inserted successfully")
            elif sub_ch.lower() == "b":
                pos=int(input("Enter position: "))
                if pos > len(lst):
                    print("position not in list")
                    continue
                data=input("Enter data: ")
                lst.insert(pos,data)
                print(f"{data} inserted at {pos} successfully")
            else:
                print("Invalid choice")
        case 2:
            data=input("Enter the data to be deleted: ")
            if data in lst:
                lst.remove(data)
                print("Data deleted successfully")
            else:
                print("data  not found!")
        case 3:
            sub_ch=input("Enter the sub choice (a or b): ")
            if sub_ch.lower() == "a":
                lst.pop()
                print("data removed from last position")
            elif sub_ch.lower()=="b":
                print("Enter the position where data is to be deleted: ")
                pos=int(input())
                if pos < len(lst):
                    lst.pop(pos)
                else:
                    print("position not in list")
        case 4:
            sub_ch=input("Enter sub choice (a or b): ")
            if sub_ch.lower()=="a":
                print(lst.sort())
            elif sub_ch.lower()=="b":
                print(lst.sort(reverse=True))
        case 5:
            print("The list in reverse order is : ")
            #print(lst)
            #print(lst.reverse())
            print(lst)
        case 6:
            print(sorted(lst))
        case 7:
            print(reversed(lst))
        case 8:
            sub_ch=input("Enter the sub choice (a or b): ")
            if sub_ch.lower() == "a":
                for ele in lst:
                    print(ele,end=" ")
            elif sub_ch.lower() == "b":
                for idx,v in enumerate(lst):
                    print(f"{idx} : {v}")
            else:
                print("invalid sub choice!")
        case 9:
            print("Exiting .....")
        case others:
            print("Invalid choice")
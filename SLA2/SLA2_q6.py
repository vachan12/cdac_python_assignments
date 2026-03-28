
choice= 0
st1=set()

while choice !=7:
    choice=int(input("""
                    1. delete element if exists otherwise
do not show any errr)
                    2.add a element
                    3.create one or more set
                    4.union of two sets
                    5.intersection of two sets
                    6.Convert set into frozen set
                    7.Exit
"""))
    match choice:
        case 1:
            element=input("Enter the element to be deleted: ")
            st1.discard(element)
            print(f"{element} deleted successfully if it existed")
        case 2:
            element=input("Enter the element to be added: ")
            st1.add(element)
            print(f"{element} added successfully")
        case 3:
            num_sets=int(input("Enter the number of sets to create: "))
            sets_list = []
            for i in range(num_sets):
                set_input = input(f"Enter elements for set {i+1} (comma separated): ")
                new_set = set(set_input.split(","))
                sets_list.append(new_set)
                print(f"Set {i+1} created successfully: {new_set}")
        case 4:
            if len(sets_list) < 2:
                print("Please create at least two sets first.")
            else:
                union_set = sets_list[0].union(sets_list[1])
                print(f"Union of set 1 and set 2: {union_set}")
        case 5:
            if len(sets_list) < 2:
                print("Please create at least two sets first.")
            else:
                intersection_set = sets_list[0].intersection(sets_list[1])
                print(f"Intersection of set 1 and set 2: {intersection_set}")
        case 6:
            if len(sets_list) == 0:
                print("Please create a set first.")
            else:
                frozen_set = frozenset(sets_list[0])
                print(f"Frozen set created from set 1: {frozen_set}")
        case 7:
            print("Exiting...")
            
        case 8:
            print("Invalid choice. Please try again.")
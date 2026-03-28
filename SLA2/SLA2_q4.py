#zip
city_list =[]
location_list = []
choice=2
while choice != 2:
    choice=int(input("""
                     1. Insert
                     2. Exit
                     Enter your choice: 
                     """))
    if choice == 1:
        city=input("Enter city name: ")
        location=input("Enter location name: ")
        city_list.append(city)
        location_list.append(location)
    elif choice == 2:
        print("Exiting the program")
    else:
        print("Invalid choice")
for zip in zip(city_list,location_list):
    print(zip)
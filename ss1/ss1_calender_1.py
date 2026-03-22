"""
User specifies the number of days in the month and starting day
need to print the calender of the month

0=Monday
1=Tuesday
2=Wednesday
3=Thursday
4=Friday
5=Saturday
6=Sunday


"""

no_of_days=int(input("Enter the number of days in the month: "))
start_day=int(input("Enter the start of the day: "))



print("Mon Tue Wed Thu Fri  sat Sun")

for i in range(start_day):
    print("   ",end="")

for date in range(1,no_of_days+1):
    print(f"{date:3}", end=" ")

    if (start_day+date)%7==0:
        print()
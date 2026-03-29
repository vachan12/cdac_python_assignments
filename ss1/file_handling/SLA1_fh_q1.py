
while True:
    with open("empdata.dat","a") as fh:
            empno=int(input("Enter employee number: "))
            name=input("Enter employee name: ")
            salary=float(input("Enter employee salary: "))
            designation=input("Enter employee designation: ")

            record = f"{empno}:{name}:{salary}:{designation}"
            fh.write(record+"\n")
            print("Do you want to Contnue adding records?(Y/N)?")
            choice=input()
            if choice.upper() != 'Y':
                break
with open("empdata.dat","r") as fh:
    for line in fh:
        empno, name, salary, designation = line.strip("\n").split(":")
        print(f"Employee Number: {empno}, Name: {name}, Salary: {salary}, Designation: {designation}")
        if designation == "Manager":
            print(f"salary: {float(salary)+float(salary)*0.1}")
        elif designation == "Clerk":
            print(f"salary: {float(salary)+float(salary)*0.05}")
        elif designation == "HR":
            print(f"salary: {float(salary)+float(salary)*0.08}")
        else:
            print(f"salary: {float(salary)+float(salary)*0.03}")
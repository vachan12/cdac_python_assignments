people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

#1.Find out how many students are there in the list
no_of_students=len(people)
print(f"Number of students in list are: {no_of_students}")

#2.Change Lisa's favourite colour
people['Lisa']='green'
print(people)

#3.Remove jenny and her favourite colour
people.pop('Jenny')
print(people)

#4.sort
for name in sorted(people):
    print(name, ":", people[name])


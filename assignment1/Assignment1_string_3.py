s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
new_str=s1[:1]+s2[:1]+s1[len(s1)//2:len(s1)//2+1]+s2[len(s2)//2:len(s2)//2+1]+s1[len(s1)-1:]+s2[len(s2)-1:]
print("The new string is ",new_str)
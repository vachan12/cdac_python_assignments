s1=input("Enter the first string: ")
s2=input("Enter the second string: ")

s1_len=len(s1)
mid=s1_len//2
new_str=s1[:mid]+s2+s1[mid:]
print("The new string is ",new_str)
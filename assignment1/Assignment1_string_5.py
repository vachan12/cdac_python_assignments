s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
i=0;j=-1
newstr=''
while(i<len(s1) and j>=-len(s2)):
    newstr=newstr+s1[i]+s2[j]
    i=i+1
    j=j-1
newstr=newstr+s1[i:]+s2[:j]
print("The new string is ",newstr)
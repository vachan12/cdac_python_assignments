#list overlapping
#overlapping lis
lst1=[1,2,3,4,5]
lst2=[1,2,3,4,5]

#non overlapping list
lst_1=[1,23,89,00,88]
lst_2=['w','v','e','u']

def overlap(lst1,lst2):
    intersect_ele=[item for item in lst1 if item in lst2]

    if(len(intersect_ele)>0):
        return True
    else:
        return False
res=overlap(lst1,lst2)
res2=overlap(lst_1,lst_2)

print(res)
print(res2)
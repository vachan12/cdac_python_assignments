# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:25:58 2026

@author: PGCP-BDA
"""

set1={10,20,30,40,50}
set2={30,40,50,60,70}

#intersection
set3=set1.intersection(set2)
print(f"Intersection: {set3}")

#differnce
set4=set1.difference(set2)
print(f"Difference: {set4}")

#union
set5=set1.union(set2)
print(f"Union: {set2}")

#symmetric_difference
set6=set1.symmetric_difference(set2)
print(f'Symmetric Difference: {set6}')

#symmetric_difference_update
set1.symmetric_difference_update(set2)
print(f'Symmetric Difference Update: {set1}')

set1.difference_update(set2)
print(f'Difference Update: {set1}')
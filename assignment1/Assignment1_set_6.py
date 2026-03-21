# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:07:51 2026

@author: PGCP-BDA
"""

set1=set({})
n=int(input('What should be the length of String?'))
print('Enter Strings: ')
for i in range(5):
    st=input()
    if(len(st)>n):
        set1.add(st)
print(set1)


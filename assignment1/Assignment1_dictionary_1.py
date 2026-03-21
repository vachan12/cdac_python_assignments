# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:21:11 2026

@author: PGCP-BDA
"""

list1=['Ten','Twenty','Thirty']
list2=[10,20,30]
dicy={}
for x,y in zip(list1,list2):
    dicy[x]=y
print(dicy)
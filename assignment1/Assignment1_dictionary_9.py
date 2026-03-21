# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:18:49 2026

@author: PGCP-BDA
"""

ename=input('Enter the name of the employee')
sal=int(input('Enter the salary'))
sampleDict = { 
'emp1': {'name': 'Jhon', 'salary': 7500}, 
'emp2': {'name': 'Emma', 'salary': 8000}, 
'emp3': {'name': 'Brad', 'salary': 6500} 
}
for k,v in sampleDict.items():
    if v["name"]==ename:
        if v["salary"]<sal:
            v["salary"]=sal
            
print(sampleDict)
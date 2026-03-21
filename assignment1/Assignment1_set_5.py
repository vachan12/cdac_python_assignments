# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:51:04 2026

@author: PGCP-BDA
"""

set1={10,20,30,40,50}
set2={30,40,50,60,70}
avg=sum(set1)/len(set1)
set1=set(filter(lambda num:num>avg,set2))
print(set1)
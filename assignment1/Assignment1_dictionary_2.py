# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:30:56 2026

@author: PGCP-BDA
"""

dict1={'Ten':10, 'Twenty':20, 'Thirty':30}
dict2={'Thirty':30, 'Fourty':40,'Fifty':50}

dict3={**dict1, **dict2}
print(dict3)
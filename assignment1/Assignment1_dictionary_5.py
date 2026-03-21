# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:44:03 2026

@author: PGCP-BDA
"""

sampleDict={'a':100, 'b':200, 'c':300, 'd':200}
sampleDict1=sampleDict


new_dict={k:v for k,v in sampleDict.items() if v!=200 }
    
print(new_dict)
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:55:13 2026

@author: PGCP-BDA
"""

guru=input("Enter String: ")
ch=0
while(ch!=5):
    ch=int(input("Enter Choice: "))
    match ch:
        case 1:
            print(guru[::2])
        case 2:
            print(guru[1::2])
        case 3:
            print(len(guru))
        case 4:
            print(guru+'a'*len(guru))
        case 5:
            print("Exiting .....")
        case others:
            print("Invalid choice ....")

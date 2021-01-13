# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 21:33:08 2021

@author: ARCHISMAN ROY
"""

import calendar

def leap(year):
        
    if(calendar.isleap(year)):
        print(str(year) + " is a leap year.")
    else:
        print(str(year) + " is not a leap year.")





Year=int(input("Enter the year:"))

leap(Year)

for k in range(2000,2022):
    if(calendar.isleap(k)):
        print(k)
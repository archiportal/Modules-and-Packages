# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:15:57 2021

@author: ARCHISMAN ROY
"""

import datetime
x = datetime.datetime.now()

print("Year: ", x.year)
print("month: " , x.month)
print("day: " , x.day)




print("time: ",x.strftime("%X"))

print("date and time: " , x.strftime("%x") + "," , x.strftime("%X"))
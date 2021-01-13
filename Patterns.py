# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:49:42 2021

@author: ARCHISMAN ROY
"""

def Pypart(n):     
    for i in range(0, n): 
        for j in range(0, i+1):           
            print("* ",end="")
        print("\r") 

def Pypart2(n): 
      
    k = 2*n - 2
  
    for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ")     
        k = k - 2      
        for j in range(0, i+1):           
            print("* ", end="")       
        print("\r") 

def Triangle(n):     
    k = 2*n - 2  
    for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ")      
        k = k - 1    
        for j in range(0, i+1):           
            print("* ", end="")    
        print("\r") 

def NumPattern(n):       
    num = 1 
    for i in range(0, n):       
        num = 1      
        for j in range(0, i+1):         
            print(num, end=" ")         
            num = num + 1
        print("\r") 

def ContinuosNum(n):      
    num = 1  
    for i in range(0, n):       
        for j in range(0, i+1):           
            print(num, end=" ")           
            num = num + 1      
        print("\r")
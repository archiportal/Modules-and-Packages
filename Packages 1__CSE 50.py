# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:35:11 2021

@author: ARCHISMAN ROY
"""

import Packages1

print('Find your information about the following creatures ')

while(1):
    print("Press\n1.For Fish\n2.For Birds\n3.For Reptiles\n4.For Amphibians\n5.For Mammals \n6.Exit\n\n")
    ch=int(input())
    if ch==1:
        Packages1.Fish.examples()
        Packages1.Fish.chars()
    elif ch==2:
        Packages1.Birds.examples()
        Packages1.Birds.chars()

    

    elif ch==3:
        Packages1.Amphibians.examples()
        Packages1.Amphibians.chars()
    
    elif ch==4:
        Packages1.Reptiles.examples()
        Packages1.Reptiles.chars()

    elif ch==5:
        Packages1.Mammals.examples()
        Packages1.Mammals.chars()

    elif ch==6:
        print('Arigato') 
        break
    else:
        print('Wrong Input.') 

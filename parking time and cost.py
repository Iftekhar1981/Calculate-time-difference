# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 15:26:42 2021

@author: 47483
"""
from datetime import datetime
import math

def solution(E,L):
    D=L-E
    total_seconds = D.total_seconds()
    ID=total_seconds/(60*60)
    
    ID=math.ceil(ID)
    cost=2+3+((ID-1)*4)
    return cost

BT=input("Enter Beginnning time: ")
ET=input("Enter Exit time: ")

print("Beginning time: ",BT)
print("Exit time: ",ET)

E = datetime.strptime(BT, '%H:%M')
L = datetime.strptime(ET, '%H:%M')

# D = L-E

# tcost=total_cost(E, L)
print("Total Parking bill is : ",solution(E, L))


# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 19:45:57 2021

@author: Josh
"""
import numpy as np

filename = 'movementdata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=str)
# print(data)
forward = 0
up = 0
aim = 0
print(data[0])
print(data[0][-1])
for i in range(len(data)):
    if data[i][0] == 'f':
        forward += int(data[i][-1])
        up += aim * int(data[i][-1])
        
    # if data[0][0] == 'b':
    #     forward -= data[0][-1]
        
    if data[i][0] == 'u':
        aim -= int(data[i][-1])
        
    if data[i][0] == 'd':
        aim += int(data[i][-1])
print(up, forward)
print(up * forward)
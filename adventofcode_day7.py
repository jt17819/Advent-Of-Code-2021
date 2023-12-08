# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:03:01 2021

@author: Josh
"""
import numpy as np


def align_crabs(pos, setTo):
    count = 0
    for i in pos:
        change = int(abs(setTo - i))
        count += change * (change + 1) // 2
    return count

filename = 'crabdata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=int).tolist()
data.sort()
# print(data) 
# print(np.mean(data))

mean = np.round(np.mean(data))
curr = align_crabs(data, mean)
below = mean - 1
above = mean + 1
one_below = align_crabs(data,below)
# print(curr)
while curr >  one_below:
    curr = one_below
    # print(curr)
    below -= 1
    one_below = align_crabs(data,below)
    
one_above = align_crabs(data,above)
while curr >  one_above:
    curr = one_above
    above += 1
    one_above = align_crabs(data,above)

# print(align_crabs(data, 2))
print(curr)
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:38:00 2021

@author: Josh
"""
import numpy as np

filename = 'fishdata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=int).tolist()
# print(data) 

def step_forward(fishes):
    new_fishes = fishes[:]
    # print(new_fishes)
    num_fish = len(fishes)
    for i in range(num_fish):
        new_fishes[i-1] = fishes[i]
        
        if i == 0:
            new_fishes[7][0] += fishes[i][0]
            
        # else:
        #     fishes[i] -= 1
    return new_fishes

day_count = []
for day in range(9):
    day_count.append([0])
print(day_count)

for fish in range(len(data)):
    for day in range(7):
        if data[fish] == day:
            day_count[day][0] += 1
print(day_count)

steps = 256
for step in range(steps):
    day_count = step_forward(day_count)
# print(day_count)
print((np.sum(day_count)))
        
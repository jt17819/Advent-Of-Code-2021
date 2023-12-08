# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:52:37 2021

@author: Josh
"""
import numpy as np

filename = 'folddata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=int)
# print(data) 

# fold along x=655
# fold along y=447
# fold along x=327
# fold along y=223
# fold along x=163
# fold along y=111
# fold along x=81
# fold along y=55
# fold along x=40
# fold along y=27
# fold along y=13
# fold along y=6

folds = [['x',655],['y',447],['x',327],['y',223],['x',163],['y',111],['x',81],
         ['y',55],['x',40],['y',27],['y',13],['y',6]]#,['x',5]]

# grid = np.zeros((15,15))

grid = np.zeros((max(data[:,1])+1,max(data[:,0])+1))

for pos in data:
    grid[pos[1],pos[0]] = 1

# print(grid)

for fold in folds:
    # print(fold)
    if fold[0] == 'x':
        for pos in data:
            if pos[0] > fold[1]:
                # print(pos[0])
                pos[0] = fold[1] - (pos[0] - fold[1])
                # print(pos[1])

        grid = np.zeros((len(grid),fold[1]))

        for pos in data:
            grid[pos[1],pos[0]] = 1
    
    if fold[0] == 'y':
        for pos in data:
            if pos[1] > fold[1]:
                # print(pos[0])
                pos[1] = fold[1] - (pos[1] - fold[1])
                # print(pos[1])

        grid = np.zeros((fold[1],len(grid[0])))

        for pos in data:
            grid[pos[1],pos[0]] = 1
            
print(grid)
print(sum(sum(grid)))
    
    
    
    
    
    
    
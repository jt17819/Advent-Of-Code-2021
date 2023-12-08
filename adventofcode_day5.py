# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 11:07:28 2021

@author: Josh
"""
import numpy as np

filename = 'griddata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=str)
# print(data[:10])
newdata = []

for i in range(len(data)):
    pos = data[i]
    if '->' in data[i]:
        pos = data[i].split(' ')
        pos.pop(1)
        newdata.append(pos[0])
        newdata.append(pos[1])
    else:
        newdata.append(pos)
# print(data[:6])
# print(newdata)

grid = np.zeros((1000,1000))

for i in range(0, len(newdata)-3, 4):
    incrementor = 1
# for i in range(0, 1, 2):
        
    if abs(int(newdata[i]) - int(newdata[i+2])) == abs(int(newdata[i+1]) - int(newdata[i+3])):
        if (int(newdata[i]) > int(newdata[i+2])) and (int(newdata[i+1]) < int(newdata[i+3])) or (int(newdata[i]) < int(newdata[i+2])) and (int(newdata[i+1]) > int(newdata[i+3])):
            
            
            if int(newdata[i]) > int(newdata[i+2]):
                newdata[i],newdata[i+1],newdata[i+2],newdata[i+3] = newdata[i+2],newdata[i+3],newdata[i],newdata[i+1]
            
            # if newdata[i] == '5' and newdata[i+1] == '5':
            #     print(newdata[i:i+4])
            #     print(grid[int(newdata[i+1]):int(newdata[i+3]),int(newdata[i]):int(newdata[i+2])])
                
            for j in range(0,abs(int(newdata[i])-int(newdata[i+2]))+1):
                grid[int(newdata[i+1])-j,int(newdata[i])+j] += 1
            
    #if abs(int(newdata[i]) - int(newdata[i+1])) == abs(int(newdata[i+2]) - int(newdata[i+3])) and newdata[i] == newdata[i+1]:
        else:
            if int(newdata[i]) > int(newdata[i+2]):
                newdata[i],newdata[i+1],newdata[i+2],newdata[i+3] = newdata[i+2],newdata[i+3],newdata[i],newdata[i+1]
                
            for j in range(0,abs(int(newdata[i])-int(newdata[i+2]))+1):
                grid[int(newdata[i+1])+j,int(newdata[i])+j] += 1
        
    if newdata[i] == newdata[i+2]:
        # print('x',newdata[i])
        if int(newdata[i+1]) > int(newdata[i+3]):
            newdata[i+1],newdata[i+3] = newdata[i+3],newdata[i+1]
        grid[int(newdata[i+1]):int(newdata[i+3])+1,int(newdata[i])] += 1
        # print(grid[int(newdata[i+1]):int(newdata[i+3])+1,int(newdata[i])])
        
    if newdata[i+1] == newdata[i+3]:
        # print(newdata[i+1])
        if int(newdata[i]) > int(newdata[i+2]):
            newdata[i],newdata[i+2] = newdata[i+2],newdata[i]
        grid[int(newdata[i+1]),int(newdata[i]):int(newdata[i+2])+1] += 1
        # print(grid[int(newdata[i+1]),int(newdata[i]):int(newdata[i+2])+1])
        
    # if abs(int(newdata[i]) - int(newdata[i+3])) == abs(int(newdata[i+1]) - int(newdata[i+2])):
    #     if int(newdata[i]) > int(newdata[i+1]):
    #         newdata[i],newdata[i+1] = newdata[i+1],newdata[i]
            
    #     for j in range(int(newdata[i]),int(newdata[i+1])+1):
    #         grid[j,int(newdata[i])+int(newdata[i+1])-j] += 1
            
    # if abs(int(newdata[i]) - int(newdata[i+1])) == abs(int(newdata[i+2]) - int(newdata[i+3])):
    #     if int(newdata[i]) > int(newdata[i+2]):
    #         newdata[i],newdata[i+2] = newdata[i+2],newdata[i]
    #     for j in range(int(newdata[i]),int(newdata[i+2])+1):
    #         grid[j,j] += 1
        
        
# print(sum(sum(grid)))
# print(grid)
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] > 1:
            count += 1
print(count)

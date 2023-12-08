# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 09:15:21 2021

@author: Josh
"""
import numpy as np


def find_low_point(data,x,y):
    left = False
    right = False
    top = False
    bottom = False
    
    if x > 0:
        if data[y][x] < data[y][x-1]:
            left = True
    else:
        left = True
        
    if x < len(data[y]) - 1:
        if data[y][x] < data[y][x+1]:
            right = True
    else:
        right = True
        
    if y > 0:
        if data[y][x] < data[y-1][x]:
            top = True
    else:
        top = True
        
    if y < len(data) - 1:
        if data[y][x] < data[y+1][x]:
            bottom = True
    else:
        bottom = True
            
    return left,right,top,bottom


def find_basin(arr,x,y,count):
    # print(arr)
    # print(count)
    if x > 0:
        if arr[y][x] < arr[y][x-1]:
            if arr[y][x-1] != 9:
                count += 1
            # arr[y][x] = -1
            count, arr = find_basin(arr,x-1,y,count)
        
    if x < len(arr[y]) - 1:
        if arr[y][x] < arr[y][x+1]:
            if arr[y][x+1] != 9:
                count += 1
            # arr[y][x] = -1
            count, arr = find_basin(arr,x+1,y,count)
        
    if y > 0:
        if arr[y][x] < arr[y-1][x]:
            if arr[y-1][x] != 9:
                count += 1
            # arr[y][x] = -1
            count, arr = find_basin(arr,x,y-1,count)
        
    if y < len(arr) - 1:
        if arr[y][x] < arr[y+1][x]:
            if arr[y+1][x] != 9:
                count += 1
            # arr[y][x] = -1
            count, arr = find_basin(arr,x,y+1,count)
    arr[y][x] = 9
    return count, arr

filename = 'floordata.txt'

data = np.loadtxt(filename, delimiter=' ', dtype=str).tolist()
# print(data)

array = []
for i in range(len(data)):
    temp = []
    for j in range(len(data[i])):
        temp.append(int(data[i][j]))
    array.append(temp)

arr = np.array(array)

lowpoints = []
total = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        # left = False
        # right = False
        # top = False
        # bottom = False
    
        # if j > 0:
        #     if data[i][j] < data[i][j-1]:
        #         left = True
        # else:
        #     left = True
            
        # if j < len(data[i]) - 1:
        #     if data[i][j] < data[i][j+1]:
        #         right = True
        # else:
        #     right = True
            
        # if i > 0:
        #     if data[i][j] < data[i-1][j]:
        #         top = True
        # else:
        #     top = True
            
        # if i < len(data) - 1:
        #     if data[i][j] < data[i+1][j]:
        #         bottom = True
        # else:
        #     bottom = True
        left,right,top,bottom = find_low_point(data,j,i)
            
        if left and right and top and bottom:
            # lowpoints.append(int(data[i][j]))
            # print(i,j)
            lowpoints.append([[i],[j]])
            total += int(data[i][j]) + 1
            
print(total)

basins = [0,0,0]

for i in range(len(lowpoints)):
    y = lowpoints[i][0]
    x = lowpoints[i][1]
    # print(x,y)
    
    count = 1
    arr = np.array(array)
    count, ans = (find_basin(arr,x[0],y[0],count))
    # print(ans)
    # print(count)
    # print(np.where(ans==-1)[0])
    # count = len(np.where(ans==-1)[0])
    if count > basins[0]:
        basins[2] = basins[1]
        basins[1] = basins[0]
        basins[0] = count
        
    elif count > basins[1]:
        basins[2] = basins[1]
        basins[1] = count
        
    elif count > basins[2]:
        basins[2] = count
        
        
print(basins)
print(basins[0] * basins[1] * basins[2])
# print(sum(lowpoints))
# print(sum(lowpoints) + len(lowpoints))
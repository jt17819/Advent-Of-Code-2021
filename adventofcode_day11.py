# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 08:07:13 2021

@author: Josh
"""
import numpy as np


def step_forward(arr):
    # arr += np.ones(arr.shape)
    # new_arr = arr[:]
    # arr += np.ones(arr.shape)
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[i])-1):
            if arr[i][j] > 9:
                for k in range(3):
                    for l in range(3):
                        if arr[i+k-1][j+l-1] != 0:
                            arr[i+k-1][j+l-1] += 1 #= arr[i+k-l][j+l-1]
                arr[i][j] = 0
            
    return arr[1:len(arr)-1,1:len(arr)-1]






filename = 'octodata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=str).tolist()
size = len(data) * len(data[0])
# print(data) 
array = np.zeros((len(data[0])+2,len(data)+2))

for i in range(len(data)):
    for j in range(len(data[i])):
        array[i+1][j+1] = int(data[i][j])
        
print(array)
iterations = 0
# count = 0
# for it in range(interations):
while True:
    count = 0
    iterations += 1
    old = np.copy(array)
    # old = array[:]
    array += np.ones(array.shape)
    
    while True:
        # old = array[:]
        # print(old)
        array[1:len(array)-1,1:len(array)-1] = step_forward(array)
        # print(array)
        if np.all(old==array):
            break
        old = np.copy(array)
        
    # count += len(np.where(array==0)[0])
    if len(np.where(array==0)[0]) == size:
        break
# print(array[1:len(array)-1,1:len(array)-1])
print(array)
# print(len(np.where(array==0)[0]))
print(iterations)









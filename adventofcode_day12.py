# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 08:46:04 2021

@author: Josh
"""
import numpy as np

filename = 'pathdata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=str).tolist()
# print(data) 

new_data = []
for i in range(len(data)):
    new_data.append(data[i].split('-'))
print(new_data)


def path_finder(arr, target):
    # print('t', target)
    paths = []
    for i in range(len(arr)):
        if arr[i][0] == target:
            paths.append(arr[i][1])
            
        elif new_data[i][1] == target:
            paths.append(arr[i][0])
    return paths




def solution(arr,location,path,history,all_paths,small_cave):
    h = history[:]
    p = path[:]
    p.append(location)
    # print('p',p)
    # print(location)
    
    if location == 'end':
        all_paths.append(p)
        return all_paths
    
    # if location in h:
    #     return all_paths
    if len(np.where(np.array(h).astype(str) == location)[0]) > 0 and location != 'start':
        if small_cave:
            return all_paths
        else:
            small_cave = True
        
        
    
    if location == 'start':
        if location not in h:
            h.append(location)
        else:
            return all_paths
        
    # if not location.isupper():
    #     if small_cave:
    #         h.append(location)
    #     else:
    #         small_cave = True
    
    if not location.isupper():
        h.append(location)
    
    new_ways = path_finder(arr,location)
    
    for way in new_ways:
            all_paths = solution(arr,way,p,h,all_paths,small_cave)
    
    
    return all_paths

history = []
path = []
all_paths = []
small_cave = False
answer = solution(new_data,'start',path,history,all_paths,small_cave)
# print(answer)
print(len(answer))









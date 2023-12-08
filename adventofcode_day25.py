# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 12:04:38 2021

@author: Josh
"""
import numpy as np
# from typing import List, Tuple, Union


def move(r, d, rb, db):
    # new_r = r[:]
    # new_d = d[:]
    new_r = np.copy(r)
    new_d = np.copy(d)
    
    index = 0
    for i in r:
        new_pos = [i[0],(i[1]+1)%rb]
        # print(new_pos not in r and new_pos not in d)
        # print(np.any(np.all(r == new_pos, axis=1)))
        # if new_pos not in r and new_pos not in d:
        if not np.any(np.all(r == new_pos, axis=1)) and not np.any(np.all(d == new_pos, axis=1)) :
            # print('move')
            new_r[index] = new_pos
        index += 1
            #new_r.append([i[0],(i[1]+1)%rb])
            # i[1] = (i[1]+1)%rb
        # else:
        #     new_r.append(i)
    index = 0
    for j in d:
        new_pos = [(j[0]+1)%db,j[1]]
        
        # if new_pos not in new_r and new_pos not in d:
        if not np.any(np.all(new_r == new_pos, axis=1)) and not np.any(np.all(d == new_pos, axis=1)) :
            new_d[index] = new_pos
        index += 1
            #new_d.append([(j[0]+1)%db,j[1]])
            # j[0] = (j[0]+1)%db
        # else:
        #     new_d.append(j)
            
    return new_r, new_d


def new_move(M):
    new_M = np.copy(M)
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == '>' and M[i,(j+1)%len(M[i])] == '.':
                # print(i,j)
                new_M[i][j] = '.'#M[i,(j+1)%len(M[i])]
                new_M[i,(j+1)%len(M[i])] = '>'#M[i][j]
    M = np.copy(new_M)
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 'v' and M[(i+1)%len(M),j] == '.':
                new_M[i][j] = '.'#new_M[(i+1)%len(M),j]
                new_M[(i+1)%len(M),j] = 'v'#new_M[i][j]
    
    return new_M

filename = 'cucumberdata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=str)
# print(data)

arr  = np.zeros((len(data),len(data[0])),dtype=str)
right = []
down = []

for i in range(len(data)):
    for j in range(len(data[i])):
        arr[i][j] = data[i][j]
        # if data[i][j] == '>':
        #     right.append([i,j])
        # if data[i][j] == 'v':
        #     down.append([i,j])
        
# print(arr)
# print(new_move(arr))
# print(new_move(new_move(arr)))
old_arr = np.zeros_like(arr)
count = 0

while not (np.array_equal(arr, old_arr)):
    old_arr = np.copy(arr)
    arr = new_move(arr)
    count += 1
print(count)
# print(right)
# print(down)
# right = np.array(right)
# down = np.array(down)

# count = 0
# old_right = np.zeros_like(right)
# old_down = np.zeros_like(down)

# while not (np.array_equal(old_right, right) and np.array_equal(old_down, down)):
# for it in range(58):
    # old_right = right[:]
    # old_down = down[:]
    # old_right = np.copy(right)
    # old_down = np.copy(down)
    # # print(right)
    # right, down = move(right,down,len(arr[0]),len(arr))
    # count += 1
    # print(right)
    # print(old_right == right and old_down == down)
    

    # print(count)
    # print(np.array_equal(old_right, right) and np.array_equal(old_down, down))
# print(move(right,down,len(arr[0]),len(arr)))


# print(arr)
    # print('next')
    # print(right)
    # print(down)


# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if [i,j] in right:
#             arr[i][j] = '>'
#         elif [i,j] in down:
#             arr[i][j] = 'v'
#         else:
#             arr[i][j] = '.'
# print(arr)
            
            
            
            
            
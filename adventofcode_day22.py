# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:33:17 2021

@author: Josh
"""
import numpy as np

filename = 'lampdata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=str)
# print(data)
# print(data[0][0])
# arr = np.zeros((100,100,100))
# for i in range(len(data)):
#     state, x_vals = data[i][0].split(' ')
#     y_vals = data[i][1]
#     z_vals = data[i][2]
    
#     # print(state, x_vals, y_vals, z_vals)
    
#     x1, x2 = x_vals.split('..')
#     # print(x1[2:])
#     for x in range(int(x1[2:]) + 50, int(x2) + 1 + 50):
#         y1, y2 = y_vals.split('..')
#         for y in range(int(y1[2:]) + 50, int(y2) + 1 + 50):
#             z1, z2 = z_vals.split('..')
#             for z in range(int(z1[2:]) + 50, int(z2) + 1 + 50):
#                 if state == 'on':
#                     arr[x][y][z] = 1
#                 else:
#                     arr[x][y][z] = 0


# print(data)
# print(arr)
# print(sum(sum(sum(arr))))

x_vals = []
y_vals = []
z_vals = []
states = []

x_min = 0
y_min = 0
z_min = 0
x_max = 0
y_max = 0
z_max = 0

for i in range(len(data)):
    state, x_val = data[i][0].split(' ')
    states.append(state)
    
    y_val = data[i][1]
    z_val = data[i][2]
    
    x1, x2 = x_val.split('..')
    x_vals.append([int(x1[2:]),int(x2)])
    if int(x1[2:]) < x_min:
        x_min = int(x1[2:])
    if int(x2) > x_max:
        x_max = int(x2)
    
    y1, y2 = y_val.split('..')
    y_vals.append([int(y1[2:]),int(y2)])
    if int(y1[2:]) < y_min:
        y_min = int(y1[2:])
    if int(y2) > y_max:
        y_max = int(y2)
        
    z1, z2 = z_val.split('..')
    z_vals.append([int(z1[2:]),int(z2)])
    if int(z1[2:]) < z_min:
        z_min = int(z1[2:])
    if int(z2) > z_max:
        z_max = int(z2)
        
print(x_vals, y_vals,z_vals)
print(x_min, y_min, z_min)
print(x_max, y_max, z_max)

x_line = np.zeros(abs(x_min)+abs(x_max)+1)
y_line = np.zeros(abs(y_min)+abs(y_max)+1)
z_line = np.zeros(abs(z_min)+abs(z_max)+1)
print(len(x_line),len(y_line),len(z_line))

# print(states)
for i in range(len(x_vals)):
    x_vals[i][0] += x_min
    x_vals[i][1] += x_min
    print(x_vals[i][0])
    print(x_vals[i][1])
    if states[i] == 'on':
        x_line[x_vals[i][0]:x_vals[i][1] + 1] = 1
    else:
        x_line[x_vals[i][0]:x_vals[i][1] + 1] = 0
    print(x_line)
        

for i in range(len(y_vals)):
    y_vals[i][0] += y_min
    y_vals[i][1] += y_min
    
    if states[i] == 'on':
        y_line[y_vals[i][0]:y_vals[i][1] + 1] = 1
    else:
        y_line[y_vals[i][0]:y_vals[i][1] + 1] = 0
        

for i in range(len(z_vals)):
    z_vals[i][0] += z_min
    z_vals[i][1] += z_min
    
    if states[i] == 'on':
        z_line[z_vals[i][0]:z_vals[i][1] + 1] = 1
    else:
        z_line[z_vals[i][0]:z_vals[i][1] + 1] = 0
        
print(x_line)
print(sum(x_line),sum(y_line),sum(z_line))


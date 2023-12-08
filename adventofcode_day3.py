# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:04:24 2021

@author: Josh
"""
import numpy as np

filename = 'binarydata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=str)
# print(data[0][0])
# print(len(data[0]))
# data = np.array(('00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010'))
answer = ''
for j in range(len(data[0])):
    print(data)
    if len(data) == 1 or len(data) == 1:
        break
    zeros = []
    ones = []
    for i in range(len(data)):
        # print(data[i][j])
        if data[i][j] == '0':
            zeros.append(data[i])
        else:
            ones.append(data[i])
    
    if len(ones) < len(zeros):
        data = zeros
    else:
        data = ones
print(data)
answer = int(data[0],2)
# data = np.array(('00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010'))
data = np.loadtxt(filename, delimiter=',', dtype=str)

for j in range(len(data[0])):
    print(data)
    if len(data) == 1 or len(data) == 1:
        break
    zeros = []
    ones = []
    for i in range(len(data)):
        # print(data[i][j])
        if data[i][j] == '0':
            zeros.append(data[i])
        else:
            ones.append(data[i])
    
    if len(zeros) > len(ones):
        data = ones
    else:
        data = zeros
print(data)
print(answer * int(data[0],2))
# print(int(answer,2))
# print(int(answer,2)^(2**len(data[0])-1))

# print(int(answer,2)*(int(answer,2)^(2**len(data[0])-1)))


            
        
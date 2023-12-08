# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 08:19:32 2021

@author: Josh
"""
import numpy as np

filename = 'displaydata.txt'

fulldata = np.loadtxt(filename, delimiter=' ', dtype=str).tolist()
# print(data[:20]) 
# print(len(data))
# print(data)
# count = 0

zero = ''
one = ''
two = ''
three = ''
four = ''
five = ''
six = ''
seven = ''
eight = ''
nine = ''

# for i in range(len(data)):
#     for j in range(1,5):
#         if len(data[i][-j]) == 2 or len(data[i][-j]) == 3 or len(data[i][-j]) == 4 or len(data[i][-j]) == 7:
#             count += 1
# print(count)


total = 0
# fulldata = data

for data in fulldata:
    zero = ''
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''
    # print(data)

    for i in range(len(data)-5):
        # print(data[i])
        if len(data[i]) == 2:
            one += data[i]
            
        if len(data[i]) == 3:
            seven += data[i]
            
        if len(data[i]) == 4:
            four += data[i]
            
        if len(data[i]) == 7:
            eight += data[i]
        
    # print(one,seven,four,eight)
    # print(data)
    
    for j in range(len(data)-5):
        # print(j)
        if len(data[j]) == 5:
            check = True
            for k in range(len(one)):
                if one[k] not in data[j]:
                    check = False
            if check:
                three += data[j]
                continue
                
            num = 0
            for l in range(len(four)):
                # print(four[l])
                if four[l] in data[j]:
                    num += 1
            if num == 2:
                two += data[j]
            if num == 3:
                five += data[j]
        
        if len(data[j]) == 6:
            sixcheck = False
            # print('six')
            for k in range(len(one)):
                # print('six',data[j])
                if one[k] not in data[j]:
                    sixcheck = True
            if sixcheck:
                six += data[j]
                continue
                
            ninecheck = True
            for m in range(len(four)):
                if four[m] not in data[j]:
                    ninecheck = False
            if ninecheck:
                nine += data[j]
                continue
            
            zero += data[j]
    
    array = np.array((zero,one,two,three,four,five,six,seven,eight,nine))
    # print('a',array)
    answer = ''
    
    for i in range(4,0,-1):
        for j in range(len(array)):
            if len(data[-i]) != len(array[j]):
                continue
            
            check = True
            for k in range(len(data[-i])):
                
                if data[-i][k] not in array[j]:
                    check = False
                    
            if check:
                answer += str(j)
    total += int(answer)
    # print(int(answer))
print(total)



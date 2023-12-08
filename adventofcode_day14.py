# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:11:45 2021

@author: Josh
"""
import numpy as np

filename = 'makedata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=str)
# print(data) 

template = data[0]

data = data[1:]

newdata = []

for i in range(len(data)):
    pos = data[i]
    if '->' in data[i]:
        pos = data[i].split(' ')
        
        pos[2] = pos[2] + pos[0][1]
        pos[1] = pos[0][0] + pos[2][0]
        newdata.append(pos)
        # newdata.append(pos[1])
    else:
        newdata.append(pos)
# print(newdata)
newdata = np.array(newdata)
# print(newdata[:,0])
# print(newdata)
# iteration = 10
# for it in range(iteration):
#     newtemplate = ''
#     for i in range(len(template)-1):
#         index = np.where(template[i:i+2] == newdata[:,0])[0][0]
#         newtemplate += template[i] + newdata[index][1] #+ template[i+1]
#     newtemplate += template[-1]
    
#     # print(newtemplate)
#     template = newtemplate

#     max_frequency = {}
#     for i in template:
#        if i in max_frequency:
#           max_frequency[i] += 1
#        else:
#           max_frequency[i] = 1
#     print(max_frequency)
#     max_num = max(max_frequency, key = max_frequency.get)
#     min_num = min(max_frequency, key = max_frequency.get)
#     print(min_num, max_num)
#     print(max_frequency[max_num] - max_frequency[min_num])

# for i in range(len(template)):

# print(newdata[:,0])

two_letter_frequency = {}

for i in range(len(newdata)):
    for j in range(3):
        two_letters = newdata[i][j]
        two_letter_frequency[two_letters] = 0



for i in range(len(template)-1):
    two_letters = template[i:i+2]
    if two_letters in two_letter_frequency:
        two_letter_frequency[two_letters] += 1
    else:
        two_letter_frequency[two_letters] = 1
        
# print(two_letter_frequency)

iteration = 40
for it in range(iteration):
    new_two_letter_frequency = two_letter_frequency.copy()
    for i in range(len(newdata)):
        new_two_letter_frequency[newdata[i][1]] += two_letter_frequency[newdata[i][0]]
        new_two_letter_frequency[newdata[i][2]] += two_letter_frequency[newdata[i][0]]
        new_two_letter_frequency[newdata[i][0]] -= two_letter_frequency[newdata[i][0]]
    two_letter_frequency = new_two_letter_frequency.copy()

# print(new_two_letter_frequency)

max_num = max(new_two_letter_frequency, key = new_two_letter_frequency.get)
min_num = min(new_two_letter_frequency, key = new_two_letter_frequency.get)
# print(min_num, max_num)
# print(new_two_letter_frequency[max_num] - new_two_letter_frequency[min_num])


letter_count = {}
for i in new_two_letter_frequency:
    if i[1] in letter_count:
        letter_count[i[1]] += new_two_letter_frequency[i]
    else:
        letter_count[i[1]] = new_two_letter_frequency[i]
    
print(letter_count)

max_num = max(letter_count, key = letter_count.get)
min_num = min(letter_count, key = letter_count.get)
print(min_num, max_num)
print(letter_count[max_num] - letter_count[min_num])



# print(newdata)
# print(two_letter_frequency[newdata[2][0]])
# key_template = {}
# for i in range(len(data)-1):
#     two_letters = template[i:i+2]
#     if two_letters in two_letter_frequency:
#         two_letter_frequency[two_letters] += 1
#     else:
#         two_letter_frequency[two_letters] = 1



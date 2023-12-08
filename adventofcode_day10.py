# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 08:09:55 2021

@author: Josh
"""
import numpy as np

filename = 'bracketdata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=str).tolist()
# print(data) 



square = 0
rounded = 0
curly = 0
angled = 0


for i in range(len(data)-1,-1,-1):
    check = True
    length = 0
    while length != len(data[i]):
        length = len(data[i])
    # for x in range(5):
        # print(data[i])
        for j in range(1,len(data[i])):
            # print(j)
            # print(data[i])
            if data[i][j] == ']':
                # print('square')
                if data[i][j-1] == '[':
                    # data[i] = str(data[i]).replace('[]','')
                    data[i] = data[i][:j-1] + data[i][j+1:]
                    # print(data[i])
                    break
                else:
                    square += 1
                    # if data[i][j-1] == '(':
                    #     rounded += 1
                    # if data[i][j-1] == '{':
                    #     curly += 1
                    # if data[i][j-1] == '<':
                    #     angled += 1
                    data = np.delete(data,i)
                    check = False
                    break
            
            if data[i][j] == ')':
                # print('rounded')
                if data[i][j-1] == '(':
                    data[i] = data[i][:j-1] + data[i][j+1:]
                    # print(data[i])
                    break
                else:
                    rounded += 1
                    # if data[i][j-1] == '[':
                    #     square += 1
                    # if data[i][j-1] == '{':
                    #     curly += 1
                    # if data[i][j-1] == '<':
                    #     angled += 1
                    data = np.delete(data,i)
                    check = False
                    break
            
            if data[i][j] == '}':
                # print('curly')
                if data[i][j-1] == '{':
                    data[i] = data[i][:j-1] + data[i][j+1:]
                    # print(data[i])
                    break
                else:
                    curly += 1
                    # if data[i][j-1] == '[':
                    #     square += 1
                    # if data[i][j-1] == '(':
                    #     rounded += 1
                    # if data[i][j-1] == '<':
                    #     angled += 1
                    data = np.delete(data,i)
                    check = False
                    break
                
            if data[i][j] == '>':
                # print('angled')
                if data[i][j-1] == '<':
                    data[i] = data[i][:j-1] + data[i][j+1:]
                    # print(data[i])
                    break
                else:
                    angled += 1
                    # if data[i][j-1] == '[':
                    #     square += 1
                    # if data[i][j-1] == '(':
                    #     rounded += 1
                    # if data[i][j-1] == '{':
                    #     curly += 1
                    data = np.delete(data,i)
                    check = False
                    break
        
        # data[i] = str(data[i]).replace('()','')
        # data[i] = str(data[i]).replace('{}','')
        # data[i] = str(data[i]).replace('<>','')
        # for j in range(len(data[i])):
        #     if data[i:i+2] == '()':
        #         data
# print(data[i])
print(square)
print(rounded)
print(curly)
print(angled)
print(rounded * 3 + square * 57 + curly * 1197 + angled * 25137)
# print(np.array(data))
scores = []
for i in range(len(data)):
    score = 0
    for j in range(len(data[i])-1,-1,-1):
        if data[i][j] == '(':
            score *= 5
            score += 1
            
        if data[i][j] == '[':
            score *= 5
            score += 2
            
        if data[i][j] == '{':
            score *= 5
            score += 3
            
        if data[i][j] == '<':
            score *= 5
            score += 4
            
    scores.append(score)
# print(scores)
# print(len(scores))
print(np.sort(scores)[len(scores)//2])
    # square = 0
    # rounded = 0
    # curly = 0
    # angled = 0
    # for j in range(len(data[i])):
    #     if data[i][j] == '[':
    #         square += 1
    #     if data[i][j] == ']':
    #         square -= 1
        
    #     if data[i][j] == '(':
    #         rounded += 1
    #     if data[i][j] == ')':
    #         rounded -= 1
        
    #     if data[i][j] == '{':
    #         curly += 1
    #     if data[i][j] == '}':
    #         curly -= 1
            
    #     if data[i][j] == '<':
    #         angled += 1
    #     if data[i][j] == '>':
    #         angled -= 1
        
        
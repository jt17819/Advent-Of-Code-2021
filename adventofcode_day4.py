# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:57:42 2021

@author: Josh
"""
import numpy as np


def makeboard(board):
    # temp = 0
    fullboard = np.zeros((5,5))
    for i in range(1,6):
        # print(board[i].split(' '))
        
        if '' in board[i].split(' '):
            temp = board[i].split(' ')
            for j in range(len(board[i].split(' '))-1,-1,-1):
                if temp[j] == '':
                    temp.pop(j)
            fullboard[i-1] = temp
        else:
            fullboard[i-1] = board[i].split(' ')
        
        # fullboard[i-1] = board[i-1]
            
    # print('t', temp)
    # print(fullboard)
    return fullboard
    

def solveboard(bingonumbers,board):
    for num in bingonumbers:
        # print(num)
        # print(int(board[4][4]))
        for i in range(len(board[0])):
            for j in range(len(board)):
                if int(board[i][j]) == int(num):
                    board[i][j] = -1
            if np.sum(board[i]) == -5:
                return board, num
            if np.sum(board[:,i]) == -5:
                return board, num
    return board, int(num)


def solution(board,num):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if newboard[i][j] != -1:
                sum += board[i][j]
    return sum * int(num)

filename = 'bingodata.txt'
data = np.loadtxt(filename, delimiter=',', dtype=str)
# print(data[0:106])
bingonumbers = data[0:100]
boards = data[100:]
# bingonumbers = np.array((7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1))
# boards = np.array([[14, 21, 17, 24, 4],[10, 16, 15, 9, 19],
#                    [18, 8, 23, 26, 20],[22, 11, 13, 6, 5],[2, 0, 12, 3, 7]])
# print(bingonumbers)
# print(boards[:7])
# print(len(makeboard(boards[:6])))
firstboard = makeboard(boards[:6])
# print(solveboard(bingonumbers, firstboard))
newboard, number = solveboard(bingonumbers, firstboard)
# sum = 0
# for i in range(len(newboard)):
#     for j in range(len(newboard[0])):
#         if newboard[i][j] != -1:
#             sum += newboard[i][j]
            
# print(sum)
# print(sum * number)
# print(solution(newboard,number))
pos = 0
for k in range(100):
    current = makeboard(boards[k*6:(k*6)+6])
    newboard, number = solveboard(bingonumbers, current)
    
    # print(np.where(bingonumbers == str(number)))
    if np.where(bingonumbers == str(number))[0][0] > int(pos):
        print(number,pos)
        answer = solution(newboard,number)
        pos = np.where(bingonumbers == str(number))[0][0]
        print(answer)




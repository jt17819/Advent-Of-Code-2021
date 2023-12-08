# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:01:10 2021

@author: Josh
"""
p1 = 10
p2 = 8
count = 1
score1 = 0
score2 = 0
rolls = 0
while score2 < 1000:
    rolls += 3
# for i in range(2):
    p1 = (p1 + count * 3 + 1 + 2)
    while p1 > 10:
        p1 -= 10
    score1 += p1
    count += 3
    
    if score1 >= 1000:
        break
    
    rolls += 3
    p2 = (p2 + count * 3 + 1 + 2)
    while p2 > 10:
        p2 -= 10
    count += 3
    score2 += p2
print(score1,score2)
print(rolls)
print(rolls * score2)
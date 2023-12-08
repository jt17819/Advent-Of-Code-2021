# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 10:10:02 2021

@author: Josh
"""
import numpy as np


def interpreter(memory, instructions, value):
    mem = memory.copy()
    for i in range(len(instructions)):
        instruction = instructions[i].split(' ')
        
        # print(instruction)
        
        if instruction[0] == 'inp':
            mem[instruction[1]] = value
            #memory[instruction[1]] = int(model[0])
            #model = model[1:]
            # print(memory)
            
        if instruction[0] == 'add':
            if instruction[2] in mem:
                mem[instruction[1]] += mem[instruction[2]]
            else:
                mem[instruction[1]] += int(instruction[2])
            # print(mem)
            
        if instruction[0] == 'mul':
            if instruction[2] in mem:
                mem[instruction[1]] *= mem[instruction[2]]
            else:
                mem[instruction[1]] *= int(instruction[2])
            # print(mem)
            
        if instruction[0] == 'div':
            if instruction[2] in mem:
                if mem[instruction[2]] != 0:
                    mem[instruction[1]] = np.trunc(mem[instruction[1]] / mem[instruction[2]])
                else:
                    print('break')
            else:
                mem[instruction[1]] = int(np.trunc(mem[instruction[1]] / int(instruction[2])))
            # print(mem)
            
        if instruction[0] == 'mod':
            if instruction[2] in mem:
                if mem[instruction[2]] > 0 and mem[instruction[1]] >= 0:
                    mem[instruction[1]] = mem[instruction[1]] % mem[instruction[2]]
                else:
                    print('break')
            else:
                mem[instruction[1]] = mem[instruction[1]] % int(instruction[2])
            # print(mem)
            
        if instruction[0] == 'eql':
            if instruction[2] in mem:
                mem[instruction[1]] = int(mem[instruction[1]] == mem[instruction[2]])
            else:
                mem[instruction[1]] = int(mem[instruction[1]] == int(instruction[2]))
    
    return mem


def each_digit(c, a, b, p):
    new_p = []
    digit_cache = []
    for i in range(9, 0, -1):
        answer = interpreter(c, data[a:b], i)
        if answer not in digit_cache:
            digit_cache.append(answer)
            # answer['path'] += str(i)
            new_p.append(p + str(i))
    
    return digit_cache, new_p


filename = 'instructiondata.txt'

data = np.loadtxt(filename, delimiter=',', dtype=str)
# print(data)
model_num = 99
model = '59998426997979'
# model = str(model_num)
iterations = 1
cache = []

for it in range(iterations):
    memory = {'w':0,'x':0,'y':0,'z':0}
    for i in range(len(data)):
        instruction = data[i].split(' ')
        
        # print(instruction)
        
        if instruction[0] == 'inp':
            memory[instruction[1]] = int(model[0])
            model = model[1:]
            # print(memory)
            
        if instruction[0] == 'add':
            if instruction[2] in memory:
                memory[instruction[1]] += memory[instruction[2]]
            else:
                memory[instruction[1]] += int(instruction[2])
            # print(memory)
            
        if instruction[0] == 'mul':
            if instruction[2] in memory:
                memory[instruction[1]] *= memory[instruction[2]]
            else:
                memory[instruction[1]] *= int(instruction[2])
            # print(memory)
            
        if instruction[0] == 'div':
            if instruction[2] in memory:
                if memory[instruction[2]] != 0:
                    memory[instruction[1]] = np.trunc(memory[instruction[1]] / memory[instruction[2]])
                else:
                    print('break')
            else:
                memory[instruction[1]] = int(np.trunc(memory[instruction[1]] / int(instruction[2])))
            # print(memory)
            
        if instruction[0] == 'mod':
            if instruction[2] in memory:
                if memory[instruction[2]] > 0 and memory[instruction[1]] >= 0:
                    memory[instruction[1]] = memory[instruction[1]] % memory[instruction[2]]
                else:
                    print('break')
            else:
                memory[instruction[1]] = memory[instruction[1]] % int(instruction[2])
            # print(memory)
            
        if instruction[0] == 'eql':
            if instruction[2] in memory:
                memory[instruction[1]] = int(memory[instruction[1]] == memory[instruction[2]])
            else:
                memory[instruction[1]] = int(memory[instruction[1]] == int(instruction[2]))
            # print(memory)
    # print('z: ', memory['z'])
    if memory['z'] == 0:
        print(model_num)
    print(memory)
    
    model_num -= 1
    model = str(model_num)
    while '0' in model:
        model_num -= 1
        model = str(model_num)
        
    # print(model)
    # print(it)
        
# print(memory)
memory = {'w':0,'x':0,'y':0,'z':0}
cache.append(memory)


start = 0
stop = 18
depth = 0
for m in range(len(cache)):
    new_cache = []
    for i in range(9, 0, -1):
        answer = interpreter(cache[m], data[start:stop], i)
        if answer not in cache:
            new_cache.append(answer)
cache = new_cache
# print(cache)
paths = ['']

one_step, paths = each_digit(memory, 0, 18, paths[0])

two_steps = []
two_steps_path = []
for s in range(len(one_step)):
    two_step, two_path = each_digit(one_step[s], 18, 36, paths[s])
    for a in range(len(two_step)):
        if two_step[a] not in two_steps:
            two_steps.append(two_step[a])
            two_steps_path.append(two_path[a])

three_steps = []
three_paths = []
for s in range(len(two_steps)):
    two_step, two_path = each_digit(two_steps[s], 36, 54, two_steps_path[s])
    for a in range(len(two_step)):
        if two_step[a] not in two_steps:
            three_steps.append(two_step[a])
            three_paths.append(two_path[a])
    

four_steps = []
four_paths = []
for s in range(len(three_steps)):
    three_step, three_path = each_digit(three_steps[s], 54, 72, three_paths[s])
    for a in range(len(three_step)):
        if three_step[a] not in three_steps:
            four_steps.append(three_step[a])
            four_paths.append(three_path[a])
            
           
# five_steps = []
# five_paths = []
# for s in range(len(four_steps)):
#     four_step, four_path = each_digit(four_steps[s], 54, 72, four_paths[s])
#     for a in range(len(four_step)):
#         if four_step[a] not in four_steps:
#             five_steps.append(four_step[a])
#             five_paths.append(four_path[a])
                        
# # print(two_steps)
# # print(two_steps_path)
# print(len(five_steps))
# print(len(five_paths))

    
    
    
    
    
    
    
    
    
        
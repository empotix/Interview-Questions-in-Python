'''
Given an array of integers. We have to find the max element of the array, 
which is at multiple places in the array and return any one of the indices 
randomly.
'''
from random import random

array = [1,4,9,7,3,9,4,7,2,7,3,0,1,2,9,6,5,7,8,9]
max_num = 0
index = []

for i in xrange(0, len(array)):
    if array[i] == max_num:
        index.append(i)
    elif array[i] > max_num:
        index = [i]
        max_num = array[i]
        
random_index = int(random()*len(index))
print(index[random_index])

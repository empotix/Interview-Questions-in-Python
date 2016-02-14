'''
Given an array of integer, find the maximum drop between two array elements, 
given that second element comes after the first one.

num = [13, 2, 23, 15, 6, 68, 19, 1, 12, 13, 100]

Max drop is 99. But answer is 67 because second element must come after first
element. Thus, (1,100) is not a valid case
'''

num = [13, 2, 23, 15, 6, 68, 19, 1, 12, 13, 100]
low = float('inf')
max_drop = 0

for n in num[::-1]:
    if n < low:
        low = n
    else:
        if n - low > max_drop:
            max_drop = n - low
            
print(max_drop)
'''
"Given an array write a function to print all triplets in the array which sum 
of 0. 
Input: Array = [-1, -3, 5, 4]
Output: -1, -3, 4"
'''

arr = [-1, -3, 5, 4]
sum_dict = {}

for i in xrange(len(arr)-1):
    sum_dict[(arr[i])] = True
    for j in xrange(i+1, len(arr)):
        if -(arr[i]+arr[j]) in sum_dict:
            print("{0},{1},{2}".format(arr[i], arr[j], -(arr[i]+arr[j])))
            

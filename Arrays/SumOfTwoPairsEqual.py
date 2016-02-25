'''
You're given an array of integers(eg [3,4,7,1,2,9,8]) Find the index of values 
that satisfy A+B = C + D, where A,B,C & D are integers values in the array. 

Eg: Given [3,4,7,1,2,9,8] array 
The following 
3+7 = 1+ 9 satisfies A+B=C+D 
so print (0,2,3,5)
'''

arr = [3,4,7,1,2,9,8]
sum_index = dict()

for i in xrange(0, len(arr)):
    for j in xrange(i+1, len(arr)):
        if (i+j) not in sum_index:
            sum_index[i+j] = (i,j)
        else:
            print("{0} {1} {2}".format(sum_index[i+j], i, j))
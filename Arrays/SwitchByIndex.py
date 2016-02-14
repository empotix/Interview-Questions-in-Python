'''
We have an array of objects A and an array of indexes B. Reorder objects in 
array A with given indexes in array B. Do not change array A's length. 

Example:
var A = [C, D, E, F, G];
var B = [3, 0, 4, 1, 2];

sort(A, B);
// A is now [D, F, G, C, E];
'''

def sort(a, b):
    
    for i in xrange(0, len(b)):
        while b[i] != i:
            j = b[i]
            a[i], a[j] = swap(a[i], a[j])
            b[i], b[j] = swap(j, b[j])
            
    print(a)
            
def swap(a,b):
    a, b = b, a
    return a, b
    
            
a = ['C', 'D', 'E', 'F', 'G']
b = [3, 0, 4, 1, 2]
sort(a, b)
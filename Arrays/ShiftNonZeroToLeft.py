'''
Write an algorithm that brings all nonzero elements to the left of the array, 
and returns the number of nonzero elements. 

Example input: [ 1, 0, 2, 0, 0, 3, 4 ] 
Example output: 4 

[1, 4, 2, 3, 0, 0, 0] 

* The algorithm should operate in place, i.e. shouldn't create a new array. 
* The order of nonzero elements does not matter 
'''

array = [ 1, 0, 2, 0, 0, 3, 4 ] 
print(array)

left = 0
right = len(array) - 1

while left < right:
    
    #If you find a non zero element while coming from the right hand side
    if array[right] > 0:
        
        #Look for an element that is 0 from the left hand side
        while (left < right) and array[left] != 0:
            left = left + 1
            
        #If you find such an element, swap them
        if array[left] == 0:
            array[left], array[right] = array[right], array[left] 
    
    left += 1
    right -= 1
    print(array)

#Number of non zero elements is the first index of 0
print(array.index(0))
    
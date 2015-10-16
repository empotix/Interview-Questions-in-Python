'''
Created on Oct 15, 2015

@author: gaurav
'''

def quickSort(num):
    return performQuickSort(num, 0, len(num)-1)

def performQuickSort(num, low, high):
    
    if (low >= high):
        return num
    
    i = low
    j = high
    pivot = num[(low+high)//2]
    print("Working with Pivot as {0}".format(pivot))
    
    while i <= j:
        
        #Move from the left to the right until we find an element greater than the pivot
        while num[i] < pivot:
            i += 1
            
        #Move from the right to the left until we find an element lesser than the pivot
        while num[j] > pivot:
            j -= 1
        
        #If we found such elements at either side of the pivot, swap them and move one index towards each other
        if (i <= j):
            num[i], num[j] = num[j], num[i]
            print(num)
            
            #Think about the significance of this step
            i += 1
            j -= 1
    
    #After the while loop is over, the selected pivot is in the right place since
    #all elements to the left are smaller than it and all elements to the right 
    #are greater than it
    print("Pivot {0} is in its right place\n".format(pivot))
    
    #If there is a part of the array from the original low to the current j, so the same for it (left part of the pivot)
    if low < j:
        performQuickSort(num, low, j)
        
    #If there is a part of the array from the current i to the original high, do the same for it (right part of the pivot)
    if high > i:
        performQuickSort(num, i, high)
        
            
if __name__ == "__main__":
    quickSort([2,10,1,8,6,5,4,7,3,9])
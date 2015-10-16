'''
Created on Oct 15, 2015

@author: gaurav
'''

def mergeSort(num):
    
    if(len(num) < 2):
        return num
    
    left = num[:len(num)//2]
    right = num[len(num)//2:]
    
    #Calls the breaking method on the left side and right side of the list
    mergeSort(left)
    mergeSort(right)
    
    print("Merging {0} and {1}".format(left, right))
    
    #Gets to this point for the first time when we have 2 one element lists and then 
    #on the recursive way back to combine 2 2-element lists and so on
    return merge(num, left, right)

def merge(dest, left, right):
    destIndex = 0
    leftIndex = 0
    rightIndex = 0
    
    #While there are elements in both lists, see which one has the lesser current one and 
    #add it to the destination and move the indexes forward
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            dest[destIndex] = left[leftIndex]
            destIndex += 1
            leftIndex += 1
        else:
            dest[destIndex] = right[rightIndex]
            destIndex += 1
            rightIndex += 1  
    
    #If there are elements left in the left array, add it to the destination
    while(leftIndex < len(left)):
        dest[destIndex] = left[leftIndex]
        destIndex += 1
        leftIndex += 1
    
    #If there are elements left in the right array, add it to the destination        
    while(rightIndex < len(right)):
        dest[destIndex] = right[rightIndex]
        destIndex += 1
        rightIndex += 1
    
    return dest
    
if __name__ == "__main__":
    print(mergeSort([5,1,3,8,7,4,6,2]))
    print(mergeSort([8,7,6,5,4,3,2,1]))
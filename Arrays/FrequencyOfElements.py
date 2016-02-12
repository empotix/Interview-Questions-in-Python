from collections import Counter

#Count frequencies of all elements in array in O(1) extra space and O(n) time
def noSpaceConstraint(num):
    
    #Use inbuilt Counter method which creates a hash map of element to frequency
    freq = Counter(num)
    print(freq)


#Count frequencies of all elements in array in O(1) extra space and O(n) time
#The idea is to traverse the given array, use elements as index and store their 
#counts at the index. For example, when we see element 7, we go to index 6 and 
#store the count. There are few problems to handle, one is the counts can get 
#mixed with the elements, this is handled by storing the counts as negative. 
#Other problem is loosing the element which is replaced by count, this is 
#handled by first storing the element to be replaced at current index.
def spaceContraint(num):
    
    i = 0
    while i < len(num):
        
        #If the current element is negative, it means its a count value and 
        #not an element of the original array
        if num[i] < 0:
            continue
        
        #Finding the index at which we will store the count of n i.e. index n-1
        elementIndex = num[i] - 1
        
        #If the element index is already negative, it means we have seen this 
        #element before. So we further negate the count by 1. 
        #We also set the current index i to be 0 since we havent seen the element
        #i+1 in the array yet. 
        #Also, we now move on to the next element.
        if num[elementIndex] < 0:
            num[elementIndex] -= 1
            num[i] = 0;
        
        #The index where the count is to be stored is holding some other element
        else:
            num[i] = num[elementIndex]
            num[elementIndex] = -1
        
        i+=1
    
    freq = dict()
    for index, number in enumerate(num):
        if(number != 0):
            freq[index+1] = number*-1
    
    print(freq)

noSpaceConstraint([1,1,1,2,3,2,4,4,2])
spaceContraint([1,1,1,2,3,2,4,4,2])
'''
Created on Oct 15, 2015

@author: gaurav
'''

def selectionSort(num):
    
    #Note that we dont go to the last element in the outer loop since at the end of 
    #all this, it will always be the max element that is left there
    for i in range(len(num)-1):
        #Considering the index under consideration as the minimum
        minIndex = i
        
        #Going from the ith index to the end to find the smallest number
        for j in range(i,len(num)):
            
            #If something is smaller than the min of the current run, swap it that position
            #This leads to the smallest number that has been discovered always being at the
            #min index
            if num[j] < num[minIndex]:
                num[j], num[minIndex] = num[minIndex], num[j]
        
        print("Smallest element of this run is {0}".format(num[minIndex]))
        print(num)
    
    
if __name__ == '__main__':
    selectionSort([3,1,2,5,4])
    print("<------------------------------------------->")
    selectionSort([9,8,7,6,5,4,3,2,1])
'''
Created on Oct 15, 2015

@author: gaurav
'''

def insertionSort(num):
    
    #This loop repeats n-1 times for n elements in a list
    for i in range(0,len(num)-1):
        
        isSwap = False
        
        #This loop assumes that everything uptill i is sorted and aims to enter the i+1th
        #element into its correct location. Thus it starts from i+1 to get the targer element
        #and goes till 0 to find the correct location in the sorted part of the array
        for j in range(i+1,0,-1):
            
            #Keep swapping elements until the target element is not smaller than something
            #Because this means that we had found its correct location
            if num[j] < num[j-1]:
                num[j-1], num[j] = num[j], num[j-1]
                isSwap = True
                print("Swapping {0} and {1}".format(num[j], num[j-1]))
                print(num)
            
            if not isSwap:
                print("No swap took place for this iteration. Which means the correct position has been found. So breaking out of inner loop")
                break;


if __name__ == '__main__':
    insertionSort([3,1,2,5,4,0])
    
'''
Created on Oct 15, 2015

@author: gaurav
'''
def bubbleSort(num):
    for i in range(len(num)-1):
        
        #The inner loop goes till len(num) - i - 1. The i is there because i elements have already been placed
        #in the correct position at the end of the list. The -1 is there because we have a num[j+1] inside, so
        #we dont want to go into the sorted section again or cause an index out of bound exception
        for j in range(0, len(num)-i-1):
            
            #If a number on the left is greater than a number on the right, swap them so that the current largest
            #element in the list bubbles to the right end
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                
            print(num)

if __name__ == '__main__':
    bubbleSort([4,5,1,3,2])
    
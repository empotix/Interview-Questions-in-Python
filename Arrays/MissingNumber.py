'''
Created on Oct 15, 2015

@author: gaurav
'''

#You have an array of integers. Each integer in the array should be listed three times in the array. 
#Find the integer which does not comply to that rule.

def main(num):
    #Take the unique elements of the list and multiply every element by 3
    n = lambda x: x*3
    y = map(n, set(num))
    
    #The difference between the ideal sum and the current sum is the missing element
    return sum(y) - sum(num)
    
if __name__ == '__main__':
    print(main([1,1,1,2,2,2,3,3]))
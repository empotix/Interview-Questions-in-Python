'''
Created on Oct 15, 2015

@author: gaurav
'''

def checkIfPowerOf2(n):
    return (n>0 and n&(n-1)==0)

def checkIfPowerOf2BitwiseShift(n):
    #If the original number is 0,1 or any negative number, it cannot be a power of 2
    if n <= 1:
        return False
    
    #Keep checking numbers remainder with 2 and dividing it by 2. 
    #If at any point, the number is not divisible by 2, it is not a power of 2
    #If it is a power of two, the last n/2 will lead to it becoming 1. So if the while
    #loop ends with the condition of n==1, the number is a power of 2
    while n!=1:
        if n % 2 != 0:
            return False
        n = n / 2
    
    #Will reach here only if the remaining number is 1, which will only happen 
    #for a power of 2, which has been divided by 2 and the last operation was 
    #2/2 which lead to n = 1
    return True
        
    
if __name__ == '__main__':

    print(checkIfPowerOf2BitwiseShift(2))
    print(checkIfPowerOf2BitwiseShift(3))
    print(checkIfPowerOf2BitwiseShift(4))
    print(checkIfPowerOf2BitwiseShift(8))
    print(checkIfPowerOf2BitwiseShift(11))
    print(checkIfPowerOf2BitwiseShift(-2))
    print(checkIfPowerOf2BitwiseShift(0))
    print(checkIfPowerOf2BitwiseShift(1))
'''
You have two numbers decomposed in binary representation, write a function 
that sums them and returns the result. 

Input: 100011, 100100 
Output: 1000111

Theory 
sum = a xor b xor c 
carry = ab + bc+ ac 
'''

input1 = [1,0,0,0,1,1]
input2 = [1,0,0,1,0,0]

def findBitwiseSum():
    sumOfBits = []
    carry = 0
    for i in xrange(len(input1)-1, -1,-1):
        sumOfBits.append(input1[i]^input2[i]^carry)
        carry = (input1[i] & input2[i]) | (input1[i] & carry) | (input2[i] & carry)
    sumOfBits.append(carry)
    print(sumOfBits[::-1])
    
findBitwiseSum()
'''
Created on Oct 15, 2015

@author: gaurav
'''

#The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. 
#These functions are throw-away functions, i.e. they are just needed where they have been created. Lambda functions are mainly 
#used in combination with the functions filter(), map() and reduce(). 
#The following example of a lambda function returns the sum of its two arguments:
#>>> f = lambda x, y : x + y
#>>> f(1,1)
#2

def lambdaXOR(num):
    
    #Lambda that XOR's two numbers
    y = lambda x,y : x^y
    ans = num[0]
    
    for n in num[1:]:
        ans = y(ans,n)
        
    print(ans) 

lambdaXOR(num = [1,2,3])
lambdaXOR(num = [1,2,3,4])
lambdaXOR(num = [1,2,3,4,5,6,7])
lambdaXOR(num = [1,2,3,4,5,6,7,8,9])


#USING REDUCE AND LAMBDA
#The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value. 
#If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
#At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
#In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
#The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
#Continue like this until just one element is left and return this element as the result of reduce()

def reduceLambdaXOR(num):
    print(reduce(lambda x,y: x^y, num))
    
reduceLambdaXOR(num = [1,2,3])
reduceLambdaXOR(num = [1,2,3,4])
reduceLambdaXOR(num = [1,2,3,4,5,6,7])
reduceLambdaXOR(num = [1,2,3,4,5,6,7,8,9])

#Other examples of uses of reduce
#Determining the maximum of a list of numerical values by using reduce:
#>>> f = lambda a,b: a if (a > b) else b
#>>> reduce(f, [47,11,42,102,13])
#102
#>>> 
#Calculating the sum of the numbers from 1 to 100:
#>>> reduce(lambda x, y: x+y, range(1,101))
#5050

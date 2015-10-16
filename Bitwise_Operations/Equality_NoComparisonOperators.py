'''
Created on Sep 20, 2015

@author: gaurav
'''

def checkEquality(a,b):
    print(a,b)
    return not(a^b)

if __name__ == '__main__':
    print(checkEquality(2,3))
    print(checkEquality(2,2))
    print(checkEquality(2,-1))
    print(checkEquality(-1,-1))
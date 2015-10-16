'''
Created on Oct 16, 2015

@author: gaurav
'''

# Given two strings A and B, the task is to convert A to B if possible. 
# The only operation allowed is to put any character from A and insert it at front. 
# Find if it is possible to convert the two stringd
# If yes, then output minimum no. of operations required for transformation.

# Input:  A = "ABD", B = "BAD"
# Output: 1
# Explanation: Pick B and insert it at front.
# 
# Input:  A = "EACBD", B = "EABCD"
# Output: 3
# Explanation: Pick B and insert at front, EACBD => BEACD
#              Pick A and insert at front, BEACD => ABECD
#              Pick E and insert at front, ABECD => EABCD

def transformString(a,b):
        
    if a == b:
        print("There are already the same form")
        return
    
    if len(set(a)) != len(set(b)):
        print("Characters are different. Not anaagrams of each other. No amount of rotation would help")
        return
    
    count = 0
    
    #TODO: NOT WORKING
    for i in xrange(len(a)-1,-1,-1):
        
        #If the current character from the end is the same, we are fine. Move on to the next
        if a[i] == b[i]:
            continue
        
        print(i)
        print(a.index(b[i]))
        count += abs(i - a.index(b[i]))
    
    print(count)
        
if __name__ == "__main__":
    #transformString("ABD","BAD")
    transformString("EACBD","EABCD")
'''
Created on Oct 13, 2015

@author: gaurav
'''

def permutations():
    results = [[]]
    num = 'abcd'
    for x in num:
        results = [r[:i] + [x] + r[i:] for r in results for i in range(len(r)+1)]
    print(results)

class Permutations(object):
    
    def __init__(self, s):
        #Dont need to declare object variables outside and then initialise them here.
        #Directly initialise them on self over here
        self.s = [ch for ch in s]
        self.used = [0 for _ in xrange(0,len(s))]
        self.out = []
        
    def permute(self):
        if len(self.out) == len(self.s):
            print(self.out)
            return
            
        for i in range(len(self.s)):
            
            #If the i has not been used in the current permutation add i to it and permute further on the remaining positions
            if self.used[i] != 1:
                self.out.append(self.s[i])
                self.used[i] = 1
                self.permute()
                
                #Now that we have returned from the recursion after hitting the base case, we can discard this i for the current run
                #and mark it as unused in this position
                self.used[i] = 0
                self.out = self.out[:-1]
                
ob = Permutations("abcd")
ob.permute()
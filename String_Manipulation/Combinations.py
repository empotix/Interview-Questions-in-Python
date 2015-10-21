'''
Created on Oct 20, 2015

@author: gaurav
'''

class Combinations(object):
    
    def __init__(self, word):
        self.word         = word
        self.combinations = []
        self.current      = []
        
    def combine(self, start_index):
        
        for i in range(start_index, len(self.word)):
            
            #Add the starting character to the current list
            self.current.append(self.word[i])
            
            #Add the sequence uptil now to the combinations list
            self.combinations.append(''.join(self.current))
            
            #Call combine to calculate combinations for the remaining positions in the word
            self.combine(i+1)
            
            #Remove the last added character and loop again to try a diffenrent combination
            self.current = self.current[:-1]
            
        return self.combinations
        
        
if __name__ == '__main__':
    ob = Combinations("abc")
    print(ob.combine(0))
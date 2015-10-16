'''
Created on Oct 16, 2015

@author: gaurav
'''

# Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible
# for every character of str1 to every character of str2 and all occurences of the character
# in str1 should map to the same character in str2
# Input:  str1 = "aab", str2 = "xxy"
# Output: True
# 'a' is mapped to 'x' and 'b' is mapped to 'y'.
# 
# Input:  str1 = "aab", str2 = "xyz"
# Output: False
# One occurrence of 'a' in str1 has 'x' in str2 and 
# other occurrence of 'a' has 'y'.

def isIsomorphic(x, y):
    if len(x) != len(y):
        return False;
    
    char_mapping = {}
    
    for i in xrange(0,len(x)):
        if x[i] in char_mapping:
            if char_mapping.get(x[i]) != y[i]:
                return False
        else:
            if y[i] in char_mapping.values():
                return False
            char_mapping[x[i]] = y[i]
    
    return True
    
if __name__ == '__main__':
    print(isIsomorphic("aab","xxyd"))
    print(isIsomorphic("aab","xxy"))
    print(isIsomorphic("aab","xxx"))
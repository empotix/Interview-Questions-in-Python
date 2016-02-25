from collections import Counter

def isPermutedSubstringInParentString(A,B):
    
    freqB = Counter(A)
    
    for i in xrange(len(B)-len(A)+1):
        
        #Checking if the current window contains a permutation of the word
        sub_string = B[i:i+len(A)]
        if Counter(sub_string) == freqB:
            return True
        
    return False

if __name__ == "__main__":
    A = "abc"
    B = "jaksjcbaksjd"
    print(isPermutedSubstringInParentString(A,B))
    
    A = "abc"
    B = "jaksjcbdaksjd"
    print(isPermutedSubstringInParentString(A,B))
    
    A = "aba"
    B = "jabkajaakb"
    print(isPermutedSubstringInParentString(A,B))
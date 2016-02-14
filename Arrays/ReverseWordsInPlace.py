'''
Code a function that receives a string composed by words separated by spaces and returns a string where words appear in the same order but than the original string, but every word is inverted. 
Example, for this input string


@"the boy ran"
the output would be


@"eht yob nar"
Tell the complexity of the solution.
'''

def linearTimelinearSpace():
    string = "the boy ran"
    string = string.split()
    
    for i in xrange(0, len(string)):
        word = list(string[i])
        left = 0
        right = len(word)-1
    
        word[left], word[right] = word[right], word[left]
        string[i] = ''.join(word)
    
    print(' '.join(string))
    
linearTimelinearSpace()
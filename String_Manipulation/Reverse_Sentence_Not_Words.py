'''
Created on Sep 23, 2015

@author: gaurav
'''
#Reverse the sentence while maintaining the directions of the words
#My name is Gaurav Keswani --> Keswani Gaurav is name My

def shortMethod(s):
    return ' '.join(s.split()[::-1])

def longMethod(s):
    sentence = ""
    word = ""
    
    for i in range(len(s)):

        if s[i] == ' ':
            sentence = word + ' ' + sentence
            word= ''
        else:
            word += s[i]
            
    sentence = word + ' ' + sentence
    return sentence         

if __name__ == '__main__':
    print(shortMethod("My name is Gaurav Keswani"))
    print(longMethod("My name is Gaurav Keswani"))
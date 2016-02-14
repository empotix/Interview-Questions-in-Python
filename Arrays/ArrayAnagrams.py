'''
Given an array of words, write a method that determines whether there are any 
words in this array that are anagrams of each other. 

Sample #1: @[@"bag", @"bat", @"tab"]; // output TRUE 
Sample #2: @[@"gab", @"bat", @"laf"]; // output FALSE
'''
from collections import Counter

#Worse case would be quadratic since for each element we can compare every
#other element of the array to check if they have the same frequency


#This solution runs in nlogn time
def containsAnagrams(array):
    words = dict()
    flag = False
    
    for word in array:
        word = ''.join(sorted(list(word)))
        if word in words:
            flag = True
            break
        else:
            words[word] = 1
            
    print(flag)

    
array = ["bag", "bat", "tab"]
array = ["gab", "bat", "laf"]
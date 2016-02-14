'''
write an algorithm to decide weather a string is a palindrome. 
Ignore any non-letter characters in the the string. 
Ignore capital/lower case. 
Space complexity O(1) 

for example, the following should return true: 
A man, a plan, a canal -- Panama!
'''
from collections import defaultdict

string = "A man, a plan, a canal -- Panama!"
string = string.lower().split()

def isValid(char):
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        return True
    return False
    
counter = defaultdict(int)

for word in string:
    for char in word:
        if isValid(char):
            counter[char] += 1

counts = counter.values()
flag = False

if sum(counts) % 2 == 0 :
    if sum([x%2 for x in counts]) == 0:
        flag = True
    
else:
    if sum([x%2 for x in counts]) == 1:
        flag = True 
    
print(flag)
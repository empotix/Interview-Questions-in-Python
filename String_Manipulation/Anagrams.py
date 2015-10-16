'''
Created on Oct 15, 2015

@author: gaurav
'''
def isAnagram(a,b):
    return len(a) == len(b) and set(a) == set(b)

if __name__ == '__main__':
    print(isAnagram("park","karp"))
    print(isAnagram("park","kar"))
    print(isAnagram("park","karpp"))
    print(isAnagram("park","abcd"))
    print(isAnagram("ppp","p"))
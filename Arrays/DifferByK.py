'''
Given an array of positive, unique, increasingly sorted numbers A, e.g. 
A = [1, 2, 3, 5, 6, 8, 9, 11, 12, 13]. Given a positive value K, e.g. 
K = 3. Output all pairs in A that differ exactly by K. 

Output:
2, 5 
3, 6 
5, 8 
6, 9 
8, 11 
9, 12 
'''

#Brute Force Method
#This is quadratic in time since for every number in the array we go
#through the enter array to check if n-3 is present
#O(n^2)
def findNumDifferingByK_BruteForce(num):
    for n in num:
        if n + 3 in num:
            print("{0},{1}".format(n, n+3))
     
#This method is better than brute force since it is linear in time 
#O(n)      
def findNumDifferingByK_Hash(num):
    hashtable = dict()
    for n in num:
        
        #Checking if a variable n-3 was set previously
        if hashtable.get(n-3, None):
            print(n-3, n)
            
        #Setting the value in the dictionary
        hashtable[n] = 1



num = [1, 2, 3, 5, 6, 8, 9, 11, 12, 13]
findNumDifferingByK_BruteForce(num)
print("")
findNumDifferingByK_Hash(num)

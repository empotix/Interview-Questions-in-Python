'''
Created on Sep 18, 2015

@author: gaurav
'''

def main(matrix):
        
    for i in range(0,len(matrix)):
        print (matrix[i])
    
    #Iterator variables
    i = 0
    j = 0
    
    #Dimension variables of current matrix. Keep track of end points of current matrix like (5,5) for a 5 x 5 array
    k = len(matrix)    #Row counter of the current matrix
    l = len(matrix[0]) #Column counter of the current matrix
    
    while i<k and j<l:
        
        #Print the top top row of the current matrix i.e. outermost starts at (0,0) and then goes to (1,1) and so on..
        for j in xrange(j,l):
            print(matrix[i][j])
        
        #Print the rightmost column of the current matrix
        for i in xrange(i+1,k):
            print(matrix[i][j])
        
        #Print the bottom row of the current matrix
        for j in range(j-1,len(matrix[0])-l-1,-1):
            print(matrix[i][j])
        
        #Print the leftmost column of the current matrix    
        for i in range(i-1, len(matrix)-k, -1):
            print(matrix[i][j])
            
        j = j + 1 #i is already at 1st row. Moving j to first column so that our current matrix becomes (1,1) from (0,0) or (2,2) from (1,1)
        k = k - 1 #Reducing the number of rows of the current matrix since we have already covered the outer layer
        l = l - 1 #Reducing the number of columns of the current matrix since we have already covered the outer layer
        
        #k and l are reduced by one even though we have covered 2 rows and 2 columns because 1 row and 1 column is reduced when we move
        #i and j from say (0,0) to (1,1)

if __name__ == '__main__':
    main([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 16]])
    main([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
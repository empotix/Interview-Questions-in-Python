'''
Created on Sep 18, 2015

@author: gaurav
'''

def printSpiralMatrix(matrix):
    '''
        Takes a two dimensional matrix as its input and prints it in spiral order
        
        Input: A list of lists 
        Returns: List of spiral output of the passed in 2 dimensional matrix
        
        Example:
            Input: [[11, 12, 13, 14, 15],[21, 22, 23, 24, 25],[31, 32, 33, 34, 35],[41, 42, 43, 44, 45]]
            Output: [11, 12, 13, 14, 15, 25, 35, 45, 44, 43, 42, 41, 31, 21, 22, 23, 24, 34, 33, 32]
    '''
    i = 0
    j = 0
    k = len(matrix) #Row count
    l = len(matrix[0]) #Column count
    spiral_output = [] #
    
    while i<k and j<l:
        
        #Print the top row of the current outermost layer of the matrix
        for j in xrange(j,l):
            spiral_output.append(matrix[i][j])
            
        #Print the right row of the current outermost layer of the matrix
        for i in xrange(i+1,k):
            spiral_output.append(matrix[i][j])
        
        #Print the bottom row of the current outermost layer of the matrix
        for j in range(j-1, len(matrix[0])-l-1,-1):
            spiral_output.append(matrix[i][j])
        
        #Print the left row of the current outermost layer of the matrix
        for i in range(i-1, len(matrix)-k,-1):
            spiral_output.append(matrix[i][j])
        
        #Peeling off the outermost layer of the matrix
        j += 1
        k -= 1
        l -= 1
        
    print(spiral_output)
    return spiral_output

if __name__ == '__main__':
    printSpiralMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 16]])
    printSpiralMatrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
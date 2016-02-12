
#Given an array A[] and a number x, check for pair in A[] with sum as x

def main(num, x):
    
    hash_table = dict()
    
    for n in num:
        
        #If the value that needs to be added to n, has already been set, it means
        #we have seen it in the past. 
        if hash_table.get(x - n):
            print("({0},{1})".format(n, x-n))
            
        #Set n for future pairs to know that it was seen
        hash_table[n] = 1
    
main([1,2,-1,4,9], 3)
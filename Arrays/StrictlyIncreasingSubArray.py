#Input: arr[] = {1, 4, 3}
#Output: 1
#There is only one subarray {1, 4}

#Input: arr[] = {1, 2, 3, 4}
#Output: 6
#There are 6 subarrays {1, 2}, {1, 2, 3}, {1, 2, 3, 4}
#                      {2, 3}, {2, 3, 4} and {3, 4}

#Input: arr[] = {1, 2, 2, 4}
#Output: 2
#There are 2 subarrays {1, 2} and {2, 4}

def main(num):
    
    print("Input Array: {0}".format(num))
    i = 0
    
    for i in range(0, len(num)-1):
        for j in range(i+1, len(num)):
            
            #If the current element if greater than the previous one, the 
            #sequence is valid and can still be valid going ahead
            if num[j] > num[j-1]:
                print(num[i:j+1])
                
            #If the current element is not greater than the previous, the 
            #sequence until now is now broken. And we need to start afresh
            else: 
                break

main([1, 4, 3])
main([1, 2, 3, 4])
main([1, 2, 2, 4])
main([1, 2, 3, 1, 5])
                
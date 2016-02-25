'''
You are given an integer K, and a sorted array as an input which has been 
rotated about an unknown pivot. For example, 4 5 6 7 8 9 1 2 3

We need to write a function which should return the index of K in the 
array, if K is present, else return -1.
'''

arr = [4,5,6,7,9,1,2,3]
num = 9

def search(low, high):
    mid = (low + high)/2
    
    if(arr[mid] == num):
        return mid
    
    #If the lower half is sorted
    if(arr[mid] > arr[low]):
        print("Lower half is sorted")
        
        #And the number is in the lower half
        if(num >= arr[low] and num <= arr[mid]):
            print("Number is in the lower half")
            return search(low, mid-1)
        else:
            print("Number is in the upper half")
            return search(mid+1, high)  
            
    if(arr[mid] < arr[high]):
        print("Upper half is sorted")
        if(num >= arr[mid] and num <= arr[high]):
            print("Number is in the upper half")
            return search(mid+1, high)
        else:
            return search(low, mid-1)
            print("Number is in the lower half")

print(search(0, len(arr)-1))
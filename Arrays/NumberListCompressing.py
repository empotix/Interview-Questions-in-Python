'''
Created on Oct 15, 2015

@author: gaurav
'''
#[1,2,3,10,25,26,31,32,33] becomes 1-3, 10, 25-26, 31-33
#[1,2,3,10,25,26,31,32,33,36] becomes 1-3, 10, 25-26, 31-33, 36

def main(num):
    
    output = []
    if len(num) < 2:
        return num
    
    #Slow is the pointer that keeps a track of the beginning of the sequence while fast tries to find the end of the sequence
    slow = 0
    fast = 0
    while(fast<len(num)-1):
        
        #If the sequence is valid, keep moving fast forward 
        if num[fast] + 1 == num[fast+1]:
            fast += 1
        
        #Once the sequence breaks, we checks if it is a one element sequency or multi element sequence
        else:
            if slow == fast:
                output.append(str(num[slow]))
            else:
                output.append("{0}-{1}".format(num[slow], num[fast]))
                
            slow = fast+1
            fast += 1
    
    #The last sequence or non-sequence will always be left since we break out of the loop
    if slow == fast:
        output.append(str(num[slow]))
    else:
        output.append("{0}-{1}".format(num[slow], num[fast]))
                
    return ", ".join(output)

if __name__ == '__main__':
    print(main([1,2,3,10,25,26,31,32,33]))
    print(main([1,2,3,10,25,26,31,32,33,36]))
    print(main([1]))
    print(main([1,2]))
    print(main([1,2,3,5]))
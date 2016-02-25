def printTripleLift(n):
    
    for i in xrange(1,n+1):
        if i % 21 == 0:
            print("Triple Lift")
        elif i % 3 == 0: 
            print("Triple")
        elif i % 7 == 0:
            print("Lift")
        else:
            print(i)
            
if __name__ == "__main__":
    printTripleLift(15)
    printTripleLift(21)           
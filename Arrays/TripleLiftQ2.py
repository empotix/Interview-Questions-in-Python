triple_liftian_numbers = {0 : 6,
                          1 : 7,
                          2 : 2}

def nthTripleLiftianNumber(n):
    
    #Using the global variable so as to perform memoization to make future calls faster
    global triple_liftian_numbers
    
    #If this is a number we have already seen before, return directly
    if triple_liftian_numbers.get(n, None):
        return triple_liftian_numbers.get(n)
    
    else:
        value = ((4 * nthTripleLiftianNumber(n-1)) - (5 * nthTripleLiftianNumber(n-2)) + (3 * nthTripleLiftianNumber(n-3)))
        triple_liftian_numbers[n] = value
        return value
    

if __name__ == "__main__":
    print(nthTripleLiftianNumber(0))
    print(nthTripleLiftianNumber(25))   
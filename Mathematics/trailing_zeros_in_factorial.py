def findTrailingZeros(n):
    '''
    Count trailing 0s in n!

    Function to return trailing 0s in factorial of n
    '''

    # initialize result
    count = 0

    # keep dividing by power of 5 and update count
    i = 5
    while (n/i >= 1):
        count += int(n/i)
        i *= 5
    
    return int(count)

# Driver program
n = 100
print("Count of trailing 0s","in 100! is", findTrailingZeros(n))

import math

def exactly_three_divisors(num):
    """
    This function shows how to calculate exactly three divisors of a given number.
    """
    primes = set()

    for i in range(2, num+1):
        if i == 2 or i==3:
            primes.add(i)
        elif i%2 == 0 or i%3 == 0:
            continue
        else:
            primes.add(i)
        count = 0
        for val in primes:
            if val * val <= num:
                count += 1
        return count


# print(exactly_three_divisors(10))

# efficient approach
def numberswiththreediv(N):
    count = 0
    i = 2
    while i*i <= N:
        # check prime
        if isPrime(i):
            # Print numbers in the order of occurrence
            count += 1
        i += 1
    print(count)

# check if a number is prime or not
def isPrime(N):
    i = 2
    while i*i <= N:
        if N%i == 0:
            return False
        i += 1
    return True

# Driver code
numberswiththreediv(10)


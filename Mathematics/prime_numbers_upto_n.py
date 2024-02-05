# naive approach
def isPrime(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True

def primes(n):
    for i in range(2, n+1):
        if isPrime(i):
            print(i, end=" ")

if __name__ == "__main__":
    n = 18
    primes(n)


# efficient approach
def prime_numbers(n):
    """
    Solving the problem using sieve of eratosthenes

    we get the prime number from 1 to N where N is the input.
    here we remove all the numbers divisible by 2,3 and 5. So that the remaining will always be prime numbers.
    """

    if n <= 1:
        return
    prime = [True] * (n+1)

    i = 2

    while i*i <= n:
        if prime[i]:
            for j in range(2 * i, n+1, i):
                prime[j] = False
        i += 1
    
    for i in range(2, n+1):
        if prime[i]:
            print(i, end=" ")

if __name__ == "__main__":
    number = 18
    prime_numbers(number)

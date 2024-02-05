# naive solution
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_factors(num):
    if num == 1:
        return 1
    for i in range(2, num+1):
        if is_prime(i):
            x = i
            while num%x == 0:
                print(i, end=" ")
                x = x * i

n = int(input("Enter n: "))
prime_factors(n)

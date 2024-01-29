def exactly_three_divisors(num):
    primes = set()

    for i in range(2, num+1):
        if i == 2 or i==3:
            primes.add(i)
        elif i%2 == 0 or i%3 == 0:
            continue
        else:
            primes.add(i)

    for val in primes:
        if val**2 < num:
            


print(exactly_three_divisors(10))

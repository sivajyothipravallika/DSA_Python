def check_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

check_prime(10)
        

# print(check_prime(19))


# efficient approach
# def prime_number_check(n):
#     if n == 1:
#         return False
#     i = 2
#     while(i * i <= n):
#         if n%i==0:
#             return False
#         i += 1
#     return True


# # super efficient approach
# def isPrime(n):
#     if n == 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n%2 == 0 or n%3==0:
#         return False
#     i = 5
#     while (i*i <= n):
#         if n%i == 0 or n%(i+2) == 0:
#             return False
#         i += 6
#     return True

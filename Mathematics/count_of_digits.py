def count_of_digits(n: int):
    count = 0
    while (n != 0):
        n = n // 10
        count+=1
    return count

# print(count_of_digits(3422))

'''
Mathemetical Formula to get the number of digits for a given number N.

number of digits in N = log10(N) + 1
'''
import math

def count_digits(n):
    count = math.log10(n) + 1
    return int(count)

print(count_digits(342223))
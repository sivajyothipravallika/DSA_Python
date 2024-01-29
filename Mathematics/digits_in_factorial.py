'''
Efficient Approach:
We are going to use log and its properties.

log 1 = 0 (Number of digit = 1)
.
.
.
.
log 10 = 1 (Number of digits = 2)
.
.
.
.
log 100 = 2 (Number of digits = 3)

'''
import math

def count_digits_in_factorial(num):
    if num < 0:
        return 0
    if num <= 1:
        return 1
    
    digits = 0
    for n in range(2, num+1):
        digits += math.log10(n)
    return math.floor(digits) + 1

print(count_digits_in_factorial(120))
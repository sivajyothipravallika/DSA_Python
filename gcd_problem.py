def greatest_common_divisor(a,b):
    '''
    function defines the euclidean algorithm to find the GCD of two given numbers.

    naive approach for this problem can be of as follows:
    -> take the a and decrease its value until the decreased number divides b.
    '''
    while a!=b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# if __name__ == "__main__":
#     a = 100
#     b = 200
#     print(greatest_common_divisor(a, b))

# naive method
def gcd(m,n):
    if m > n:
        small = n
    else:
        small = m
    for i in range(1, small+1):
        if((m%i==0) and (n%i==0)):
            res = i
    return res

# print(gcd(12,15))

# euclidean method
def computeGCD(x,y):
    while(y):
        x,y = y,x%y
    return abs(x)


# more efficient approach
def gcd_cal(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

import math

math.gcd(12,15)
# naive approach
def divisors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i, end=" ")

'''
Efficient solution can be based on the following two ways.

1. Division always appear in pairs
ex: 30: (1,30), (2,15), (3,10), (5,6)

2. one of the divisions in every pair is smaller than or equal to sqrt(n)

for a pair (x,y)
x*y=n
let x be the smaller, i.e., x<=y
x*x <= n
x <= sqrt(n)
'''
def divisors(num):
    i = 1
    while(i*i<=num):
        if (num%i == 0):
            print(i)
        i += 1
    while (i>=1):
        if(num%i==0):
            print(num/i)
        i -= 1

divisors(13)
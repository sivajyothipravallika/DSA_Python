# naive approach
def compute_power(x, n):
    return x ** n

# print(compute_power(2, 3))

# naive approach
def calculate_power(x, n):
    res = 1

    for i in range(n):
        res = res * x
    return res

# efficient approach
def power(x, n):
    if n==0:
        return 1
    temp = power(x, n//2)
    temp = temp * temp
    if n%2 == 0:
        return temp
    else:
        return temp * x

print(power(20, 2))

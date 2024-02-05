def multiplication_inverse(a,m):
    if a < 0 or a >= m:
        return None
    
    for x in range(1,m):
        if (a*x)%m == 1:
            return x
    return None

print(multiplication_inverse(3, 11))

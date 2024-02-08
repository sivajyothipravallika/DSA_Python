import math

def quadratic_roots(a,b,c):
    '''
    quadratic roots formulae is -b + math.sqrt(abs(val))
    '''

    discriminant = b*b - 4*a*c
    sqrt_val = math.sqrt(abs(discriminant))

    if discriminant < 0:
        return [-1]
    elif discriminant == 0:
        return [-b/(2*a)]
    else:
        return [(-b+sqrt_val)/(2*a), (-b-sqrt_val)/(2*a)]
    

print(quadratic_roots(1, -7, 12))
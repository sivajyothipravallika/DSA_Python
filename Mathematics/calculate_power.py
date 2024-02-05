def calculate_power(num, exponent):
    res = 1
    while num > 0:
        if num % 2 != 0:
            res = res * exponent
            num = num // 2
        return res
    
    print(calculate_power(2, 4))
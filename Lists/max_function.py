def max_func(l:list):
    max = l[0]
    for num in l:
        if num > max:
            max = num
    
    return max


print(max_func([40]))
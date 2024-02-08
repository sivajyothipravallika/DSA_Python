def elements_less_than_N(l:list, N:int):
    less_than_input = []
    for num in l:
        if num < N:
            less_than_input.append(num)
    
    return less_than_input



print(elements_less_than_N([8,100,20,40,3,7], 10))
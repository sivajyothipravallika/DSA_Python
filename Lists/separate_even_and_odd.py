def separate_even_and_odd(l:list):
    even_num = []
    odd_num = []
    for num in l:
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)
    return even_num, odd_num




print(separate_even_and_odd([12,3,4,5,231,4,244,5,212,12,424,1213124,676,5,7,8,6]))
print(separate_even_and_odd([2,4,6,8,10]))
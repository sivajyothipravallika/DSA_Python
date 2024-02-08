def even_odd_comprehension(l:list):
    even = [num for num in l if num%2 == 0]
    odd = [num for num in l if num%2 != 0]
    return even, odd

l = [10,3,20,5,12]
even,odd = even_odd_comprehension(l)
print(even, odd)
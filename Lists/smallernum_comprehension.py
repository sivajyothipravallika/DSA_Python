def smallernum_comprehension(l:list, n:int):
    return [num for num in l if num < n]

l = [9,15,12,3,7,11]
x = 10

print(smallernum_comprehension(l,x))

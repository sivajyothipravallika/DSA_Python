def smallernum(arr,x):
    count = 0
    for num in arr:
        if num < x:
            count += 1
    return count


print(smallernum([2,2,2,2,2], 3))
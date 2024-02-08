def greaterthanX(arr,x):
    count = 0
    for num in arr:
        if num > x:
            count += 1
    return count


print(greaterthanX([4,5,3,1,2], 3))
print(greaterthanX([2,2,2,2,2,2], 3))

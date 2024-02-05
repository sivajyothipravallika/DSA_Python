def getByIndex(arr, n, idx):
    if idx >= n:
        return -1
    else:
        return arr[idx]


print(getByIndex([41,80,8,41,5,21,32,91,54,82,43,64,76,77,70,84,24,15,70,31,65,46,31,94,15,100,70,48,43,62,31,24,81,4,59,33], 36, 2175))
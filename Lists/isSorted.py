def isSorted(l:list):
    sorted_list = sorted(l)
    if sorted_list == l:
        return 1
    elif sorted_list[::-1] == l:
        return 1
    else:
        return 0

print(isSorted([40,39,39,38,37]))
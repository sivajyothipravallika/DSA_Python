# naive approach which returns the sorted list of the input list
def sort_list(l:list):
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            if l[i] >= l[j]:
                l[i], l[j] = l[j],l[i]
    return l

print(sort_list([10, 5 , 2]))


# naive approach which returns True if the list is sorted using loop
def sortList(l:list):
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i += 1
    return True

print(sortList([1,2,3,4,5]))
print(sortList([10,2,34,2,12]))

# method-2 using sorted()
def isSorted(l:list):
    sorted_list = sorted(l)
    if sorted_list == l:
        return True
    else:
        return False

print(isSorted([1,2,3,4,5]))
print(isSorted([10,2,34,2,12]))


def immediate_smaller(arr,x):
    '''
    Function that gets the number smaller than the given input 'x' and returns the immediate number to 'x'
    '''
    l = []
    for num in arr:
        if x > num:
            l.append(num)
    
    if len(l) == 0:
        return -1
    else:
        return max(l)

# print(immediate_smaller([4,67,13,12,15], 16))
print(immediate_smaller([1,2,3,4,5],1))

# naive solution (two traversal)
def getSecMax(l:list):
    if len(l) <= 1:
        return None
    lar = getMax(l)
    sec_lar = None
    for x in l:
        if x != lar:
            if sec_lar == None:
                sec_lar = x
            else:
                sec_lar = max(sec_lar, x)
    return sec_lar

def getMax(l):
    res = l[0]
    for i in range(1, len(l)):
        res = max(res, l[i])
    return res


# efficient solution (one traversal)
def getSecMax(l:list):
    if len(l) <= 1:
        return None
    large = l[0]
    sec_large = None
    for x in l[1:]:
        if x>large:
            sec_large = large
            large = x
        elif x != large:
            if sec_large == None or sec_large < x:
                sec_large = x
    return sec_large

# naive solution because we are creating a new list from the input list which is time-consuming
def second_largest_num(l:list):
    new_l = [i for i in l if i != max(l)]
    return max(new_l) if new_l else None


print(second_largest_num([10,5,8,20,3,5,4,323,1234]))
print(second_largest_num([20,10,20,8,12]))
print(second_largest_num([10,10,10]))
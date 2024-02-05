# using built-in functions
def avgoflist(arr):
    return sum(arr) / len(arr)

# using naive approach
def avg(arr):
    sum = 0
    for x in arr:
        sum += x
    n = len(arr)
    return sum/n

print(avgoflist([30, 60, 40]))
print(avgoflist([10,20,30,40]))
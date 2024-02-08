import math

def mean(A,N):
    return int(sum(A)/N)

def median(A,N):
    A.sort()
    if N%2 != 0:
        return A[math.floor(N/2)]
    else:
        # return A[math.floor((N/2) + mean(A,N)/2)]
        return math.floor((A[int((N-1)/2)] + A[int(N/2)])/2.0)


print(mean([1,2,19,28,5], 5))
print(median([1,2,19,28,5], 5))
print(median([2,8,3,4],4))
    
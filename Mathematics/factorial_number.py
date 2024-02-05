# def factorial(n):
#     res = 1
#     for i in range(2, n+1):
#         res = res * i
#     return res

#     # if n == 0:
#     #     return 1
#     # elif n == 1:
#     #     return 1
#     # else:
#     #     return n * factorial(n-1)

# if __name__ == "__main__":
#     number = 5
#     print(factorial(number))


class Solution:
    def factorial(self, N):
        if N == 0:
            return 1
        else:
            return N * Solution.factorial(N-1)
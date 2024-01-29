# def sum_of_num(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum


# print(sum_of_num(3))
# print(sum_of_num(5))


def savings_of_n_days():
    n = int(input())
    return int(n*(n+1)/2)

print(savings_of_n_days())
def palindrome_number(num):
    res = 0
    temp = num

    while temp != 0:
        last_digit = temp % 10
        res = res * 10 + last_digit
        temp = temp // 10
    
    return res == num

print(palindrome_number(123454321))

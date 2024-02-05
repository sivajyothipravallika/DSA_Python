def isPalindrome(n:int):
    rev = 0
    temp = n
    '''
    here we are traversing from right to left.
    '''
    while temp != 0:
        last_digit = temp % 10
        rev = rev * 10 + last_digit
        temp = temp // 10
    return rev == n

if __name__ == "__main__":
    number = 4554
    print(isPalindrome(number))

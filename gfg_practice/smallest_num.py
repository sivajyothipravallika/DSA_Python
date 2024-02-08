def smallest_num():
    num = 6047

    if num % 20 == 7:
        if num % 42 == 7:
            if num % 76 == 7:
                return num

print(smallest_num())
#!/usr/bin/python3

# function for check prime


def check_prime(num):
    if num == 1 or num == 0:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= num:
        if num % i == 0:
            return False

        i += w
        w = 6 - w
    return True
# calc sum all prime below two million

num_limit = 2000000

sum_num = 0
for i in range(num_limit+1):
    if check_prime(i):
        sum_num += i
print('final sum_num: ', sum_num)

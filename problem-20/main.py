#!/usr/bin/python3

# factorial function


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

# sum calculation


def sum_calc(num):
    num_str = str(num)
    result = 0
    for i in num_str:
        result += int(i)
    return result

print(sum_calc(factorial(100)))

#!/usr/bin/python3

# declare functions


def sum_square(num):
    result = 0
    for i in range(num):
        result += (i+1)**2
    return result


def square_sum(num):
    result = 0
    for i in range(num):
        result += (i+1)
    result = result**2
    return result


# define the number
num_limit = 100
diff = abs(sum_square(num_limit) - square_sum(num_limit))
print(diff)

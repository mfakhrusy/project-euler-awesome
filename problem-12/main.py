#!/usr/bin/python3

import itertools
#  function for factorization


def factorize(num):
    counter = 2
    if num == 1:
        result = [1]
        return result
    else:
        result = []
        while num != 1:
            if num % counter == 0:
                result.append(counter)
                num = num / counter
            else:
                counter = counter + 1
        return result


# function for divisors


def divisor_v2(factor_num, num):
    result = factor_num[:]
    range_total = len(result)

    # generate combination
    for index in range(1, range_total+1):
        for subset in itertools.combinations(factor_num, index):
            tmp = 1
            for j in subset:
                tmp *= j
            result.append(tmp)
    result.append(1)
    return sorted(list(set(result)))

divisor_limit = 500
divisor = 0
num = 1
counter = 1

while divisor <= divisor_limit:
    divisor = 0
    num_old = num
    counter = counter + 1
    num = num_old + counter
    num_divisor = divisor_v2(factorize(num), num)
    divisor = int(len(num_divisor))

print(num)

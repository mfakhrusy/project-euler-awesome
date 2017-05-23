#!/usr/bin/python3

from functools import reduce

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


def divisorGen(n):
    factors = list(factorize(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


# function for divisors


def divisor_v2(factor_num, num):
    result = factor_num[:]
    for i in range(len(factor_num) - 1):
        #  generate inner range
        inner_range = list(range(len(factor_num)))
        inner_range = inner_range[i+1:]
        for j in inner_range:
            tmp = factor_num[i] * factor_num[j]
            if tmp not in result:
                result.append(tmp)
    result.append(1)
    result.append(num)
    return sorted(list(set(result)))


def divisor_count(num):
    counter = 1
    result = []
    while counter <= num/2:
        if num % counter == 0:
            result.append(counter)
        counter += 1
    result.append(num)
    return result

divisor_limit = 10
divisor = 0
num = 1
counter = 1

while divisor <= divisor_limit:
    divisor = 0
    num_old = num
    counter = counter + 1
    num = num_old + counter
#    if num % 2 == 0:
#    num_factor = factorize(num)
#    num_divisor = divisor_v2(num_factor, num)
    num_divisor = divisorGen(num)
    divisor = int(len(num_divisor))
    print(num, divisor, num_divisor)

print(num)

#!/usr/bin/python3

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


def mult_even(num):
    result = 1
    for i in range(num):
        i_factor = factorize(i+1)
        tmp_result = result
        #  iterize over factored i
        for j in i_factor:
            #  check wheter factored i (each) is a factor of result
            if tmp_result % j != 0:
                result *= j
                tmp_result = result
            else:
                tmp_result = tmp_result / j

    return result

print(mult_even(20))

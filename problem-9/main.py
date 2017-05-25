#!/usr/bin/python3
import sys

# solve using euclid, for a^2 + b^2 = c^2:
# a = m^2 - n^2
# b = 2mn
# c = m^2 + n^2
# for m = 1,2,3,4,... and n = 1,2,3, ... m - 1


def calc_a(m, n):
    return m**2 - n**2


def calc_b(m, n):
    return 2*m*n


def calc_c(m, n):
    return m**2 + n**2

num_limit = 1000
m = 2

while True:
    num_check = 0
    for n in range(1, m):
        a = calc_a(m, n)
        b = calc_b(m, n)
        c = calc_c(m, n)

        num_check = a + b + c
        if num_check == num_limit:
            # forcefully exit the code!!! XD
            print(a, b, c, num_check, 'product: ', a*b*c)
            sys.exit()
    m += 1

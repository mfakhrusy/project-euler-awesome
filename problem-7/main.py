#!/usr/bin/python3


def prime_check(num):

    # generate range check
    check = list(range(num+1))
    # delete 0 and 1 and num from the list
    check = check[2:int(len(check)-1)]

    # loopin in check-list (pun not-intended!)
    for i in check:
        if num % i == 0 and i != num:
            return False
    return True

num_counter = 2
max_count = 10001
counter = 0
biggest_prime = 2

while counter < max_count:
    if prime_check(num_counter):
        counter += 1
        biggest_prime = num_counter
    num_counter += 1

print(counter, biggest_prime)

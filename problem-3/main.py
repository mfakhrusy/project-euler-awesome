#!/usr/bin/python3

num_limit = 600851475143
denum = 2
factor = []

while num_limit != 1:
    if num_limit % denum == 0:
        factor.append(denum)
        num_limit = num_limit / denum
        denum = 2
    else:
        denum += 1

# check if prime
denum = 2
biggest_prime_factor = None
for i in factor:
    while denum <= i:
        if i % denum == 0:
            if i == denum:
                biggest_prime_factor = denum
        denum += 1

print(biggest_prime_factor)

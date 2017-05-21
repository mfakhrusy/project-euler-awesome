#!/usr/bin/python3

limit = 4000000
counter_new = 2
counter = counter_new
counter_old = 1
sum_all = 0

while True:
    counter_tmp = counter_new
    if counter_new > limit:
        break
    counter = counter_new
    counter_new = counter_new + counter_old
    counter_old = counter_tmp

    if counter % 2 == 0:
        sum_all = sum_all + counter

print('The value: ', sum_all)

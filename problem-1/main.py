#!/usr/bin/python3

max_num = 1000
counter = 1
sum_all = 0
while counter < max_num:
    if (counter % 3 == 0) or (counter % 5 == 0):
        sum_all = sum_all + counter
    counter += 1
print(sum_all)

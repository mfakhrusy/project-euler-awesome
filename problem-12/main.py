#!/usr/bin/python3

# read the input file from the problem-set -> do not change the problem-set file
path = 'problem-set.md'
file_input = open(path, 'r')
list_file = file_input.readlines()
list_file = list_file[2:]

big_num = []

# delete trailing \n
count = 0
for i in list_file:
    list_file[count] = i[:int(len(i)-1)]
    count += 1

# work on the summation
sum_big_num = 0
for i in list_file:
    sum_big_num += int(i)

# change to string
sum_big_num_str = str(sum_big_num)

# pickout the first 10 digit:
sum_big_num_str = sum_big_num_str[:10]

print(sum_big_num, sum_big_num_str)

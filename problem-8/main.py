#!/usr/bin/python3

# read the input file from the problem-set -> do not change the problem-set file
path = 'problem-set.md'
file_input = open(path, 'r')
list_file = file_input.readlines()
list_file = list_file[2:int(len(list_file)-2)]

num_1000 = []

# delete trailing \n
count = 0
for i in list_file:
    list_file[count] = i[:int(len(i)-1)]
    count += 1

# make another list containing each integer
for num in list_file:
    for i in num:
        num_1000.append(i)

digit_limit = 13
biggest_num = 1
for i in range(len(num_1000) - (digit_limit - 1)):
    tmp_list_file = num_1000[i:(i + (digit_limit))]
    tmp_biggest_num = 1
    for j in tmp_list_file:
        tmp_biggest_num *= int(j)
    if tmp_biggest_num > biggest_num:
        biggest_num = tmp_biggest_num

print(biggest_num)

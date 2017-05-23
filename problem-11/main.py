#!/usr/bin/python

pow_limit = 1000
base_num = 2

result = base_num**pow_limit
result_str = str(result)

# change the result_str into list of numbers
result_str_list = []
for i in range(len(result_str)):
    result_str_list.append(result_str[i])

# calculate the summation of the numbers
result_sum = 0
for i in result_str_list:
    result_sum += int(i)

print(result_sum)

#!/usr/bin/python3

num_1_old = 999
num_2_old = 999

num_1 = num_1_old
num_2 = num_2_old

# check if number == palindrome


def check_palindrome(num):
    num_str = str(num)
    # check if even or odd
    if len(num_str) % 2 == 0:

        num_str_1 = num_str[int(len(num_str)/2):]

    else:

        num_str_1 = num_str[int(len(num_str)/2+1):]

    num_str_2 = num_str[:int(len(num_str)/2)]
    # reverse num_str_2
    num_str_2_reversed = num_str_2[::-1]

    # check if num_str 1 == num_str_2_reversed
    if num_str_1 == num_str_2_reversed:
        return True
    else:
        return False

# num_str_1 = num_str[]

# looping for num_1 and num_2
biggest_palindrome = 1
while num_1 > 0 and num_2 > 0:
    tmp_num = num_2 * num_1
    tmp_palindrome = biggest_palindrome
    if check_palindrome(tmp_num):
        if tmp_num > tmp_palindrome:
            biggest_palindrome = tmp_num

        # print(num_1, num_2, tmp_num)
    num_1 -= 1
    if (num_1 == 0):
        num_2 -= 1
        num_1 = num_1_old

print(biggest_palindrome)

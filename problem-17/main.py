#!/usr/bin/python
from math import floor

# generate function for calculating letter count of  a number


def letter_count(num):
    letter_dict = dict([(0, 'zero'),
                        (1, 'one'),
                        (2, 'two'),
                        (3, 'three'),
                        (4, 'four'),
                        (5, 'five'),
                        (6, 'six'),
                        (7, 'seven'),
                        (8, 'eight'),
                        (9, 'nine'),
                        (10, 'ten'),
                        (11, 'eleven'),
                        (12, 'twelve'),
                        (13, 'thirteen'),
                        (14, 'fourteen'),
                        (15, 'fifteen'),
                        (16, 'sixteen'),
                        (17, 'seventeen'),
                        (18, 'eighteen'),
                        (19, 'nineteen'),
                        (20, 'twenty'),
                        (30, 'thirty'),
                        (40, 'forty'),
                        (50, 'fifty'),
                        (60, 'sixty'),
                        (70, 'seventy'),
                        (80, 'eighty'),
                        (90, 'ninety')])

    if num >= 0 and num <= 19:
        return len(letter_dict[num])
    elif num > 19 and num <= 99:
        num_tenth = floor(num/10)
        num_oneth = num % 10
        if num_oneth == 0:
            return len(letter_dict[num_tenth*10])
        else:
            tmp = len(letter_dict[num_tenth*10]) + len(letter_dict[num_oneth])
            return tmp
    elif num > 99 and num <= 999:
        # length of word 'hundred'
        tmp = len('hundred')
        num_hundredth = floor(num/100)
        num_tenth = floor((num % 100)/10)
        num_oneth = num % 10
        if num_oneth == 0:
            if num_tenth == 0:
                tmp += len(letter_dict[num_hundredth])
                return tmp
            else:
                tmp += len(letter_dict[num_hundredth]) + len('and') + \
                    len(letter_dict[num_tenth*10])
                return tmp
        elif num_tenth == 0:
            tmp += len(letter_dict[num_hundredth]) + len('and') + \
                len(letter_dict[num_oneth])
            return tmp
        elif num_tenth == 1:
            tmp += len(letter_dict[num_hundredth]) + len('and') + \
                len(letter_dict[num_tenth*10 + num_oneth])
            return tmp
        else:
            tmp += len(letter_dict[num_hundredth]) + len('and') + \
                len(letter_dict[num_tenth*10]) + len(letter_dict[num_oneth])
            return tmp
    else:
        #  case 1000 only!!!!
        return len('onethousand')

result = 0
num_limit = 1000
for i in range(1, num_limit+1):
    print(i, letter_count(i))
    result += letter_count(i+1)

print(result)

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def match_desire_number(s):
    pass

def formingMagicSquare(s):
    # Write your code here
    print(s)
    sum_of_row = []
    sum_of_column = []
    diagonal_left_to_right = 0
    diagonal_right_to_left = 0

    for index in range(len(s)):
        diagonal_left_to_right += s[index][index]
        diagonal_right_to_left += s[index][len(s) - index - 1]
        sum_of_row.append(sum(s[index]))

    n = len(s[0])  # Number of columns
    for col in range(n):
        sum_of_col = sum(s[row][col] for row in range(len(s)))  # Sum each column
        sum_of_column.append(sum_of_col)

    all_sums = [diagonal_left_to_right, diagonal_right_to_left, sum_of_column, sum_of_row]

    flat_array = [item for sublist in all_sums for item in (sublist if isinstance(sublist, list) else [sublist])]

    grouping = {}
    for number in flat_array:
        if grouping.get(number):
            grouping[number] += 1
        else:
            grouping[number] = 1

    # grouping = dict(sorted(grouping.items(), key=lambda item:item[1], reverse=True))
    max_value = max(grouping.values())
    if max_value > 1:
        desire_number = max(grouping, key=grouping.get)
    else:
        desire_number = min(grouping)

    print(desire_number, s[0])
    for index in range(len(s)):






    # if it's high, then operation should be addition
    # if it's low, then operation should be subtraction


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s= [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

    result = formingMagicSquare(s)

    print(result)

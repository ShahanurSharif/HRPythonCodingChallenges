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

def formingMagicSquare(s):
    # Write your code here
    sum_of_row = []
    diagonal_left_to_right = 0
    diagonal_right_to_left = 0
    for index in range(len(s)):
        sum_of_row.append(sum(s[index]))
        for row_index in range(len(s[index])):
            if index == row_index:
                diagonal_left_to_right += s[index][row_index]

    print(sum_of_row, diagonal_left_to_right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

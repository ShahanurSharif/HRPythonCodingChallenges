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
def magicNumber(length):
    total = length(length*length + 1)/2
    return total


def formingMagicSquare(s):
    length = 0
    length = len(s[0])
    magic_number = magicNumber(length)
    print(s[0])




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s= [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

    result = formingMagicSquare(s)

    print(result)

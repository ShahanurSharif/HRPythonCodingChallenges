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
def magicNumber(length=0):
    total = length*(length*length + 1)/2
    return int(total)

def is_magic_square(s):
    pass

def formingMagicSquare(s):
    length = len(s[0])
    magic_number = magicNumber(length)
    if is_magic_square(s):
        return 0

    pass





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s= [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

    result = formingMagicSquare(s)

    print(result)

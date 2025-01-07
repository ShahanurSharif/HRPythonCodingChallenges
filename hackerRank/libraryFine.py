#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    print(d1, m1, y1, d2, m2, y2)
    total = 0
    if y1 != y2:
        total = (y1 - y2) * 10000
    elif m1 != m2:
        total = (m1 - m2) * 500
    else:
        total = (d1 - d2) * 15

    print(total)
    if total >= 0:
        return total
    else:
        return 0

if __name__ == '__main__':
    first_multiple_input = [31, 5, 2014]
    second_multiple_input = [1, 5, 2014]
    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    print(result)

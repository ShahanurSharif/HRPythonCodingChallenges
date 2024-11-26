#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def right_most_value(a):
    return math.ceil(math.sqrt(a))


def left_most_value(b):
    return math.floor(math.sqrt(b))


def squares(a, b):
    # Write your code here
    lowest = right_most_value(a)
    highest = left_most_value(b)
    numbers = []
    for i in range(lowest, highest + 1):
        value = i ** 2
        print(value)
        numbers.append(value)

    return len(numbers)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    print(k, height)
    max_value = max(height)
    if max_value>k:
        score_required = max_value - k
    else:
        score_required = 0

    return score_required

    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # first_multiple_input = input().rstrip().split()
    #
    # n = int(first_multiple_input[0])
    #
    # k = int(first_multiple_input[1])
    #
    # height = list(map(int, input().rstrip().split()))
    k = 4
    height = [1, 6, 3, 5, 2]
    result = hurdleRace(k, height)

    # fptr.write(str(result) + '\n')

    # fptr.close()

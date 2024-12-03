#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    count = 0
    i=0
    while i<len(c):
        if (0 <= i+2 < len(c)) and c[i+2] == 0:
            i=i+2
            count += 1
        elif (0 <= i+1 < len(c)) and c[i+1] == 0:
            i=i+1
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    c= [0, 0, 1, 0, 0, 1, 0]

    result = jumpingOnClouds(c)

    print(result)

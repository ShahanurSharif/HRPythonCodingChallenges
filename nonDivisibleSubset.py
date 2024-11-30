#!/bin/python3

import math
import os
import random
import re
import sys
from enum import unique
from itertools import permutations


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # print(k, s)
    s.sort()
    print(s)
    sorted_value = s.copy()
    permutations_value = []
    for i in range(len(s)):
        new_value = []
        for x in range(i + 1, len(s)):
            if (s[i] + s[x]) % k != 0:
                new_value.append(s[i])
        permutations_value.extend(new_value)


    return len(set(permutations_value))


if __name__ == '__main__':

    k = 15

    s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]

    result = nonDivisibleSubset(k, s)

    print(result)

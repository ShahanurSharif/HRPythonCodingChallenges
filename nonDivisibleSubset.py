#!/bin/python3

import math
import os
import random
import re
import sys
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
    print(k, s)
    permutations_value = []
    for i in range(len(s)):
        new_value = [s[i] + s[x] for x in range(i + 1, len(s))]


    print(permutations_value)

if __name__ == '__main__':

    k = 3

    s = [1, 7, 2, 4]

    result = nonDivisibleSubset(k, s)

    print(result)

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
    for_process = s.copy()
    # print(for_process)
    permutations_value = []
    for i in range(len(s)):
        for x in range(i + 1, len(s)):
            # print(s[i], s[x], s[i] + s[x])
            if (s[i] + s[x]) % k == 0:
                print(s[i], s[x], s[i] + s[x])
                value = s[x]
                # print(value)
                s = [x for x in s if x != value]

    # print(for_process)
    return len(s)


if __name__ == '__main__':

    k = 3

    s = [1, 7, 2, 4]

    result = nonDivisibleSubset(k, s)

    print(result)

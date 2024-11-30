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
    print(s)
    i = 0
    while i < len(s):
        x = i + 1
        while x < len(s):  # Inner loop
            # print('i=', s[i], 'x=', s[x])
            if (s[i] + s[x]) % k == 0:
                del s[x]  # Safe because we are iterating in reverse
            else:
                x += 1  # Only increment `x` if no deletion
        i += 1
    return len(s)


if __name__ == '__main__':

    k = 3

    value = "278 576 496 727 410 124 338 149 209 702 282 718 771 575 436"
    s= list(map(int, value.split()))

    result = nonDivisibleSubset(k, s)

    print(result)

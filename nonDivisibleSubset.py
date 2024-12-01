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
    # print(s)
    diviable_k = []
    not_diviable_k = []
    for i in range(len(s)):
        for x in range(i+1, len(s)):
            if (s[i]+s[x])%k == 0:
                diviable_k.append(s[x])
            else:
                not_diviable_k.append(s[x])

    print(set(diviable_k), set(not_diviable_k))


if __name__ == '__main__':

    k = 3

    value = "278 576 496 727 410 124 338 149 209 702 282 718 771 575 436"
    s= list(map(int, value.split()))

    result = nonDivisibleSubset(k, s)

    print(result)

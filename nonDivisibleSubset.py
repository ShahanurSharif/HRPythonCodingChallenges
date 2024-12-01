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
    # Step 1: Compute remainders
    remainder_count = [0] * k
    for num in s:
        remainder_count[num % k] += 1
        print(num, k, num%k, remainder_count)



if __name__ == '__main__':

    k = 7

    value = "278 576 496 727 410 124 338 149 209 702 282 718 771 575 436"
    s= list(map(int, value.split()))

    result = nonDivisibleSubset(k, s)

    print(result)

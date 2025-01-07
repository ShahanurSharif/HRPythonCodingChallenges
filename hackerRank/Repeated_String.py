#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    count_a = s.count('a')
    len_s = len(s)

    # Calculate how many full repetitions of `s` fit in `n`
    full_repeats = n // len_s
    remainder = n % len_s

    # Count 'a' in the remainder
    remainder_a = s[:remainder].count('a')

    # Total count of 'a'
    return full_repeats * count_a + remainder_a


if __name__ == '__main__':

    s = "abba"

    n = 554045874191

    result = repeatedString(s, n)

    print(result)

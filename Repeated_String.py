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
    len_s = len(s)
    count_a = s.count('a')

    if n<len_s:
        count_a = s[0:n].count('a')
        return count_a

    total_number = math.floor(n/len_s * count_a)
    print(total_number)
    reminder = n%len_s
    print(s[0:7])

    remaining = 0
    if reminder > 0:
        remaining = s[0:reminder].count('a')

    return total_number+remaining


if __name__ == '__main__':

    s = "cfimaakj"

    n = 554045874191

    result = repeatedString(s, n)

    print(result)

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    len1 = len(s)
    len2 = len(t)
    if len1 > len2:
        calculated_len = len1
    elif len2 > len1:
        calculated_len = len2
    else:
        calculated_len = len1

    first_index = None
    for i in range(calculated_len):
        if (i < len(s) and i < len(t)) and s[i] != t[i]:
            first_index = i
            break

    unmatched_string_length = len(s[first_index:len(s)])
    required_step_to_fill = len(t[first_index:len(t)])
    if first_index is None or first_index==0:
        total_step = unmatched_string_length + required_step_to_fill + 1
        if total_step <= k:
            return "Yes"
    else:
        total_step = unmatched_string_length + required_step_to_fill
    if total_step == k:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s = input()
    #
    # t = input()
    #
    # k = int(input().strip())
    s="zzzzz"
    t="zzzzzzz"
    k = 4
    result = appendAndDelete(s, t, k)

    print(result)

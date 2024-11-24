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
    len_s = len(s)
    len_t = len(t)
    unmatched = 0
    required_steps = 0
    if len_s < len_t:
        total_steps = process_steps(len_s, len_t, s, t)
        if total_steps<=k:
            return "Yes"
        else:
            return "No"

    if len_s >= len_t:
        total_steps = process_steps(len_s, len_t, s, t)
        # print(total_steps)
        # if total_steps<=k:
        #     return "Yes"
        # else:
        #     return "No"

def process_steps(len_s, len_t, s, t):
    first_index = None
    for i in range(len_s):
        if s[i] != t[i]:
            first_index = i
            break


    unmatched = s[first_index:len_s]
    required_steps = t[first_index:len_t]
    total_steps = unmatched + required_steps
    return len(total_steps)


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

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
    index = None
    min_count = min(len_s, len_t)
    if len_s + len_t < k: return "Yes"
    for i, j in zip(s, t):
        if s[i]!=t[j]:
            index = i
            break
    if index>=0:
        min_count = len_s - index + len_t - index


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s = input()
    #
    # t = input()
    #
    # k = int(input().strip())


    s="y"
    t="yu"
    k = 2
    result = appendAndDelete(s, t, k)

    print(result)

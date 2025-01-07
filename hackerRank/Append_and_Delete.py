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
    if len_s + len_t < k:
        return "Yes"
    count = 0
    for i, j in zip(s, t):
        if i == j:
            count += 1
        else:
            break

    t_len = len_s + len_t
    if t_len<=count*2+k and t_len%2==k%2 or t_len<k:
        return "Yes"

    return "No"


    # ashley
    # abdd
    # k =4


if __name__ == '__main__':
    s = "hackerhappy"
    t = "hackerrank"
    k = 9
    result = appendAndDelete(s, t, k)

    print(result)

#!/bin/python3

import math
import os
import random
import re
import sys
from operator import indexOf


#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    next_string = "no answer"
    w_arr = list(w)
    # print(w_arr)

    i = len(w_arr) - 2
    while not (i < 0 or w_arr[i] < w_arr[i + 1]):
        i -= 1

    if i < 0:
        return "no answer"

    j = len(w_arr) - 1
    while not (w_arr[j] > w_arr[i]):
        j-=1

    # print(i, j)
    w_arr[i], w_arr[j] = w_arr[j], w_arr[i]

    w_arr[i+1:] = reversed(w_arr[i+1:])

    return "".join(w_arr)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    alphabets = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y z".split(', ')

    T = 5

    for T_itr in range(T):
        w = "ab,bb,hefg,dhck,dkhc".split(',')

        result = biggerIsGreater(w[T_itr])

        print(result)

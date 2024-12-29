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
    print(w)

    i = len(w) - 2
    while not (i < 0 or w[i] < w[i + 1]):
        i -= 1

    if i < 0:
        return "no answer"

    j = len(w) - 1
    while not (w[j] > w[i]):
        j-=1




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    alphabets = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y z".split(', ')

    T = 6

    for T_itr in range(T):
        w = "lmno,dcba,dcbb,abdc,abcd,fedcbabcd".split(',')

        result = biggerIsGreater(w[T_itr])

        # print(result)

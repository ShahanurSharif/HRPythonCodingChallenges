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
    length = len(w)
    print('b'<'a')



    return next_string

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    alphabets = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y z".split(', ')

    T = 6

    for T_itr in range(T):
        w = "lmno,dcba,dcbb,abdc,abcd,fedcbabcd".split(',')


        result = biggerIsGreater(w[T_itr])

        # print(result)

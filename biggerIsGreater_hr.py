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
    index_value = []
    for i in range(length):
        index_value.append(indexOf(alphabets, w[i]))


    for i in reversed(range(len(index_value)-1)):
        if index_value[i] < index_value[i+1]:
            print(i, index_value[i], index_value[i+1])
            break
        else:
            return False



    return next_string

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    alphabets = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y z".split(', ')

    T = 6

    for T_itr in range(T):
        w = "lmno,dcba,dcbb,abdc,abcd,fedcbabcd".split(',')


        result = biggerIsGreater(w[T_itr])

        # print(result)

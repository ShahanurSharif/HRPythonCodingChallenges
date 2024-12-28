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


    while length>=2:
        last_index = length-1
        if index_value[last_index]>index_value[last_index-1]:
            print(index_value, last_index, last_index-1, index_value[last_index], index_value[last_index-1])
            last_value = index_value[last_index-1]
            previous_value = index_value[last_index]
            index_value[last_index] = last_value
            index_value[last_index-1] = previous_value
            next_string = "".join([alphabets[value] for value in index_value ])
            break
        else:
            length -= 1

    return next_string

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    alphabets = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y z".split(', ')

    T = 6

    for T_itr in range(T):
        w = "lmno,dcba,dcbb,abdc,abcd,fedcbabcd".split(',')


        result = biggerIsGreater(w[T_itr])

        print(result)

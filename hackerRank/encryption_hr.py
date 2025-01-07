#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    length = len(s)
    x_root = math.sqrt(length)
    x_row = math.floor(x_root)
    x_col = math.ceil(x_root)
    new_string = ""
    k=0
    for i in range(0, length):
        if i<x_col:
            for j in range(0, length):
                if (j+x_col-i)%x_col==0:
                    if k!=i:
                        new_string += ' '+s[j]
                    else:
                        new_string += s[j]
                    k=i

    return new_string


if __name__ == '__main__':
    s = "haveaniceday"
    result = encryption(s)
    print(result)

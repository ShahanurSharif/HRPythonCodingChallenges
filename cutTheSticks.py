#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    new_arr = arr.copy()
    total_cut = []
    while len(new_arr)!=0:
        total = 0
        low = min(new_arr)
        total_cut.append(len(new_arr))
        for i in range(len(new_arr)):
            new_arr[i] = new_arr[i] - low
        new_arr = [x for x in new_arr if x != 0]

    return total_cut


if __name__ == '__main__':

    arr = [5, 4, 4, 2, 2, 8]

    result = cutTheSticks(arr)

    print(result)

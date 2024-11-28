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
    low = min(new_arr)
    total_cut = []
    while len(new_arr)!=1 and new_arr[0]!=1:
        total = 0
        for i in range(len(new_arr)):
            new_arr[i] = new_arr[i] - low
            total += low
            if new_arr[i] == 0:
                del new_arr[i]

        total_cut.append(total)




if __name__ == '__main__':

    arr = [5, 4, 4, 2, 2, 8]

    result = cutTheSticks(arr)

    print(result)

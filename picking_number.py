#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    sorted_a = sorted(a)
    group_arr = []
    for i in range(len(sorted_a)):
        initial_value = sorted_a[i]
        next_value = sorted_a[i+1]
        diff = initial_value - next_value



# Write your code here

if __name__ == '__main__':

    a = "4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97"

    number_array = list(map(int, a.split()))

    # print(len(number_array))

    result = pickingNumbers(number_array)

    print(result)

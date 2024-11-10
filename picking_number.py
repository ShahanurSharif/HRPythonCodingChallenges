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
group_arr = []
def generate_arr(value):
    for i in range(len(group_arr)):
        initial_value = group_arr[i][0]
        last_value = group_arr[i][-1]
        initial_diff = abs(initial_value-value)
        last_diff = abs(last_value-value)
        # print(group_arr[i], initial_value, initial_diff, last_value, last_diff, value)
        if initial_diff >=0 and last_diff <=1:
            group_arr[i].append(value)
        else:
            group_arr.append([value])

    # print(group_arr)

def pickingNumbers(a):
    sorted_a = sorted(a)
    group_arr.append([a[0]])
    for i in range(1, len(sorted_a)):
        generate_arr(sorted_a[i])

# Write your code here

if __name__ == '__main__':

    a = "4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97"

    number_array = list(map(int, a.split()))

    # print(len(number_array))

    result = pickingNumbers(number_array)

    print(group_arr)

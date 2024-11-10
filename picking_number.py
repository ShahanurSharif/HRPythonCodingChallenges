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
    found = False
    for i in range(len(group_arr)):
        initial_value = group_arr[i][0]
        last_value = group_arr[i][-1]
        initial_diff = abs(initial_value-value)
        last_diff = abs(last_value-value)
        # print(group_arr[i], initial_value, initial_diff, last_value, last_diff, value)
        if initial_diff <=1 and last_diff <=1:
            group_arr[i].append(value)
            found=True
            print(group_arr[i], initial_diff, last_diff, value)
            break

    if not found:
        group_arr.append([value])

def pickingNumbers(a):
    sorted_a = sorted(a)
    group_arr.append([sorted_a[0]])
    for i in range(1, len(sorted_a)):
        generate_arr(sorted_a[i])

    max_number = []
    for i in range(len(group_arr)):
        max_number.append(len(group_arr[i]))

    sorted_max_number = sorted(max_number, reverse=True)
    print(group_arr, sorted_max_number[0])


# Write your code here

if __name__ == '__main__':

    a = "1 2 2 3 1 2"

    number_array = list(map(int, a.split()))

    # print(len(number_array))

    result = pickingNumbers(number_array)

    # print(sorted(group_arr))

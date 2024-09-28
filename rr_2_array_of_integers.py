#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def is_dividable(value, arr):
    for item in arr:
        if value % item != 0:
            return False
    return True


def is_divisable(value, arr):
    for item in arr:
        print(f"from {arr}: {item}, value: {value}")
        if item % value != 0:
            return False
    return True

# # Check if the value divides all elements in the array
# def is_divisable(value, arr):
#     for item in arr:
#         print(f"from {arr}: {item}, value: {value}")
#         if item % value != 0:   # If any item is not divisible by value
#             return False        # Return False immediately
#     return True
def getTotalX(a, b):
    max_value_from_a = max(a)
    min_value_from_b = min(b)
    possible_numbers = []
    for i in range(max_value_from_a, min_value_from_b + 1):
        possible_numbers.append(i)

    # print(possible_numbers)
    values = []
    for value in possible_numbers:
        if is_dividable(value, a) and is_divisable(value, b):
            values.append(value)

    # print(values)
    return len(values)


arr=[1]
brr=[72, 48]
value = getTotalX(arr, brr)
print(value)
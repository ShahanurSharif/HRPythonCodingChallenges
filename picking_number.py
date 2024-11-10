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
    pass

def pickingNumbers(a):
    sorted_a = sorted(a)
    for i in range(len(sorted_a)-1):
        initial_value = sorted_a[i]
        next_value = sorted_a[i+1]
        diff = initial_value - next_value
        if diff == 0 or diff == 1:
            if len(group_arr)==0:
                group_arr.append(initial_value)
            else:
                generate_arr()

# Write your code here

if __name__ == '__main__':

    a = "4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97"

    number_array = list(map(int, a.split()))

    # print(len(number_array))

    result = pickingNumbers(number_array)

    print(result)

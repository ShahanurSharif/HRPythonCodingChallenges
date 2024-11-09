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
    total = 0
    values = {}
    for i in range(len(a)):
        # print(a, a[:1+i], a[i+1:])
        first_portion = a[:1+i]
        rest_portion = a[i+1:]
        if len(first_portion) and len(rest_portion):
            for j in range(len(rest_portion)):
                diff = abs(first_portion[-1] - rest_portion[j])
            # print(first_portion, rest_portion, first_portion[-1], rest_portion[0])
            #     print(first_portion[-1], rest_portion[0], diff, i+1+j, rest_portion[j], a[i+1+j])
                if diff==0 or diff==1:
                    if len(values)==0:
                        values[i] = a[i]
                        values[i+1+j] = a[i+1+j]
                    else:
                        values[i+1+j] = a[i+1+j]
        print(values.values())
    return len(values)



# Write your code here

if __name__ == '__main__':

    a = "4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97"

    number_array = list(map(int, a.split()))

    # print(len(number_array))

    result = pickingNumbers(number_array)

    print(result)

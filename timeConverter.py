#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s.split(':')[0]
    minute = s.split(':')[1]
    second = s.split(':')[2]
    second_value_only = second[:2]

    meridiem = second[2:]


    hour_str = hour
    if meridiem == 'PM' and hour != '12':
        hour_str = int(hour) + 12

    if meridiem == 'AM' and hour == '12':
        hour_str = int(hour) - 12

    # print(f"{hour_str}:{minute}:{second_value_only}")

    return f"{hour_str}:{minute}:{second_value_only}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

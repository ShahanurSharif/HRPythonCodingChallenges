#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
# Write your code here
# day_n1_viewed = math.floor(n/2)
# shared_n1 = day_n1_viewed*3
# day_n2_viewed = math.floor(shared_n1/2)
# shared_n2 = day_n2_viewed*3
# day_n3_viewed = math.floor(shared_n2/2)
# ...
# ....

def viralAdvertising(n):
    pass

# for i in range(1, n+1):
#     doExpand

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # 1 3 1
    #-> 0 1 1 1 2
    # 2 1 2
    #-> 2 2 1 0 0
    # 3 3 3
    #-> 0 0 0 1 1 1 2 2 2

    #0 2 1
    #-> 0 1 1 2
    #1 1 1
    #-> 2 1 0 2
    #2 0 0
    #-> 0 0

    pass


if __name__ == '__main__':

    container =[[1, 1], [1, 1]]

    result = organizingContainers(container)
    print(result)

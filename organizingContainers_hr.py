#!/bin/python3

import math
import os
import random
import re
import sys

from PIL.ImageOps import contain


#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    length = len(container)
    total = list(map(sum, zip(*container)))
    print(total)




if __name__ == '__main__':

    # container =[[1, 3, 1], [2, 1, 2], [3, 3, 3]]
    container =[[0, 2, 1], [1, 1, 1], [2, 0, 0]]

    result = organizingContainers(container)
    print(result)

#!/bin/python3

import math
import os
import random
import re
import sys

from PIL.ImageOps import contain
from numpy.lib.user_array import container


#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    column_total = sorted(list(map(sum, zip(*container))))
    row_total = sorted(list(map(sum, container)))
    print(row_total, column_total)
    # print(column_total)
    if column_total != row_total:
        return 'Impossible'

    return "Possible"



if __name__ == '__main__':

    container =[
        [1, 3, 1],
        [2, 1, 2],
        [3, 3, 3]
    ]
    # container =[[0, 2, 1], [1, 1, 1], [2, 0, 0]]

    result = organizingContainers(container)
    print(result)

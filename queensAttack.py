#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def createRows(n, queen, obstacle):
    x = [q_space for q_space in range(n)]
        # 4, 3


def createColumns(n, queen, obstacle):
    pass


def createDialonal(n, queen, obstacle):
    pass


def queensAttack(n, k, r_q, c_q, obstacles):
    createRows(n,[r_q, c_q], obstacles)
    createColumns(n,[r_q, c_q], obstacles)
    createDialonal(n,[r_q, c_q], obstacles)


if __name__ == '__main__':
    # 5
    # 3
    # 4
    # 3[[5, 5], [4, 2], [2, 3]]


    n = 5

    k = 4


    r_q = 4

    c_q = 3

    obstacles = [[5, 5], [4, 2], [2, 3]]

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)

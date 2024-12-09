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
    number_of_rows = []
    for i in obstacle:
        if queen[0] == i[0]:
            if queen[1] > i[1]:
                number_of_rows = [[queen[0], j] for j in range(queen[1], n + 1) if j != queen[1]]
            elif queen[1] < i[1]:
                number_of_rows = [[queen[0], j] for j in range(1, i[1]) if j != queen[1]]
            else:
                number_of_rows = [[queen[0], j] for j in range(1, n + 1) if j != queen[1]]
    return number_of_rows


def createColumns(n, queen, obstacle):
    number_of_columns = []
    for i in obstacle:
        if queen[1] == i[1]:
            if queen[0] > i[0]:
                number_of_columns = [[j, queen[1]] for j in range(i[1], n+1) if j!=queen[1]]
            elif queen[0] < i[0]:
                number_of_columns = [[j, queen[1]] for j in range(queen[1], n+1) if j!=queen[1]]
            else:
                number_of_columns = [[j, queen[1]] for j in range(1, n + 1) if j != queen[1]]
    return number_of_columns

#4, 3
# diagonal = [4, 3][[3, 2], [2, 1], [5, 4]]
def expand_obstacles(obstacle_matches, arr):
    expanded_obstacles = []
    for om in obstacle_matches:
        if om[0]>arr[0] and om[1]>arr[1]:
            expanded_obstacles.append([arr[0], arr[1]])

    return expanded_obstacles

def createDiagonal(n, queen, obstacle):
    diagonal = []
    obstacle_matches = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i-j == queen[0] - queen[1]:
                diagonal.append([i, j])
                if [i, j] in obstacle and [i, j] not in obstacle_matches: obstacle_matches.append([i, j])
            if i+j == queen[1] + queen[0]:
                diagonal.append([i, j])
                if [i, j] in obstacle and [i, j] not in obstacle_matches: obstacle_matches.append([i, j])
            expand_obstacles = expand_obstacles(obstacle_matches, [i, j])
    # 5, 5-> 43 32 21
    return diagonal

# [3, 2]
def queensAttack(n, k, r_q, c_q, obstacles):
    number_of_rows = createRows(n, [r_q, c_q], obstacles)
    number_of_columns = createColumns(n, [r_q, c_q], obstacles)
    number_of_diagonals = createDiagonal(n, [r_q, c_q], obstacles)

    return len(number_of_rows) + len(number_of_columns)



if __name__ == '__main__':
    # 5
    # 3
    # 4
    # 3[[5, 5], [4, 2], [2, 3]]

    n = 5

    k = 4

    r_q = 4

    c_q = 3

    obstacles = [[5, 5], [4, 2], [2, 3], [3, 2]]

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)

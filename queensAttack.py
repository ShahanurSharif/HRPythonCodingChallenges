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
    if len(obstacle)==0:
        return [[queen[0], j] for j in range(1, n+1) if j!=queen[0]]

    for i in obstacle:
        if queen[0] == i[0]:
            if queen[1] > i[1]:
                number_of_rows = [[queen[0], j]
                    for j in range(queen[1], n + 1) if j != queen[1]]
            elif queen[1] < i[1]:
                number_of_rows = [[queen[0], j]
                    for j in range(1, i[1]) if j != queen[1]]
            else:
                number_of_rows = [[queen[0], j]
                    for j in range(1, n + 1) if j != queen[1]]
    return number_of_rows


def createColumns(n, queen, obstacle):
    number_of_columns = []
    if len(obstacle)==0:
        return [[j, queen[1]] for j in range(1, n+1) if j!=queen[1]]
    
    for i in obstacle:
        if queen[1] == i[1]:
            if queen[0] > i[0]:
                number_of_columns = [[j, queen[1]]
                    for j in range(i[1], n+1) if j != queen[1]]
            elif queen[0] < i[0]:
                number_of_columns = [[j, queen[1]]
                    for j in range(queen[1], n+1) if j != queen[1]]
            else:
                number_of_columns = [[j, queen[1]]
                    for j in range(1, n + 1) if j != queen[1]]
    return number_of_columns


# 4, 3
# diagonal = [4, 3][[3, 2], [2, 1], [5, 4]]
expanded_obstacles = []


def expand_obstacles(obstacle_matches, arr):
    for om in obstacle_matches:
        # bottom left
        if om[0] > arr[0] and om[1] > arr[1]:
            expanded_obstacles.append([arr[0], arr[1]])
        # # 45-> 36->27 bottom right
        if om[0] > arr[0] and om[1] < arr[1]:
            expanded_obstacles.append([arr[0], arr[1]])
        # 45->54->63->72 top left
        if om[0] > arr[0] and om[1] < arr[1]:
             expanded_obstacles.append([arr[0], arr[1]])
        # 45->56->67 top right
        if om[0] < arr[0] and om[1] < arr[1]:
            expanded_obstacles.append([arr[0], arr[1]])
    return expanded_obstacles

def createDiagonal(n, queen, obstacle):
    diagonal=[]
    obstacle_matches=[]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i-j == queen[0] - queen[1]:
                diagonal.append([i, j])
                if [i, j] in obstacle and  [i, j] not in obstacle_matches: obstacle_matches.append([i, j])
            if i+j == queen[1] + queen[0]:
                diagonal.append([i, j])
                if [i, j] in obstacle and [i, j] not in obstacle_matches: obstacle_matches.append([i, j])
            if len(obstacle_matches):
                expand_obstacles(obstacle_matches, [i, j])
    return diagonal

# [3, 2]
def queensAttack(n, k, r_q, c_q, obstacles):
    number_of_rows=createRows(n, [r_q, c_q], obstacles)
    # print('number of rows', number_of_rows)
    number_of_columns=createColumns(n, [r_q, c_q], obstacles)
    # print('number of columns', number_of_columns)
    number_of_diagonals = createDiagonal(n, [r_q, c_q], obstacles)
    
    items_to_remove = expanded_obstacles+obstacles+[[r_q, c_q]]
    # print(number_of_diagonals, items_to_remove, number_of_rows, number_of_columns)
    total_diagonals = [item for item in number_of_diagonals if item not in items_to_remove]
    
    return len(number_of_rows)+len(number_of_columns)+len(total_diagonals)


if __name__ == '__main__':
# 5 3
# 4 3
# 5 5
# 4 2
# 2 3

    n=4

    k=0

    r_q=4

    c_q=4

    obstacles=[]

    result=queensAttack(n, k, r_q, c_q, obstacles)
    print(result)

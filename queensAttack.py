#!/bin/python3

import math
import os
import random
import re
import sys



def createRows(n, queen, obstacle):
    if len(obstacle):
        indexes = [i for i, sub in enumerate(obstacles) if sub[0] == queen[0]]
        for i in indexes:
            value = obstacles[i]
            if queen[1] > value[1]:
                return n - 1 - value[1]
            elif queen[1] < value[1]:
                return n - 1 - queen[1] + 1
            else:
                return n - 1
    else:
        return n - 1

def createColumns(n, queen, obstacle):
    if len(obstacle):
        indexes = [i for i, sub in enumerate(obstacles) if sub[1] == queen[1]]
        for i in indexes:
            value = obstacles[i]
            if queen[0] > value[0]:
                return n - 1 - value[0]
            elif queen[0] < value[0]:
                return n - 1 - queen[0] + 1
            else:
                return n - 1
    else:
        return n - 1



def createDiagonal(n, queen, obstacle):
    diff = abs(queen[0] - queen[1])
    bl_tr = n - (queen[1] - queen[0])
    tl-br = queen[0] + queen[1] - 1
    
def queensAttack(n, k, r_q, c_q, obstacles):
    number_of_rows = createRows(n, [r_q, c_q], obstacles)
    number_of_columns=createColumns(n, [r_q, c_q], obstacles)
    # number_of_diagonals = createDiagonal(n, [r_q, c_q], obstacles)

    # items_to_remove = expanded_obstacles+obstacles+[[r_q, c_q]]
    # # print(number_of_diagonals, items_to_remove, number_of_rows, number_of_columns)
    # total_diagonals = [item for item in number_of_diagonals if item not in items_to_remove]

    # return len(number_of_rows)+len(number_of_columns)+len(total_diagonals)


if __name__ == '__main__':
    # 5 3
    # 4 3
    # 5 5
    # 4 2
    # 2 3

    n = 5

    k = 3

    r_q = 4

    c_q = 3

    obstacles = [
        [5, 5],
        [4, 2],
        [2, 3],
    ]

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)

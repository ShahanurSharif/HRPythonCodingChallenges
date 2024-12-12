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
    obstacles = set(obstacle)

    def count_steps(di, dj):
        steps = 0
        x, y = queen[0] + di, queen[1] + dj
        closest_obstacle = None
        
        while 1 <= x <= n and 1 <= y <= n:  # Stay within bounds
            if (x, y) in obstacles:  # Stop if an obstacle is encountered
                closest_obstacle = (x, y)
                break
            steps += 1
            x += di
            y += dj
        
        # If no obstacle was found, return all the possible steps
        return steps


    down_right = count_steps(1, 1)  # ↘
    up_left = count_steps(-1, -1)   # ↖
    up_right = count_steps(-1, 1)   # ↗
    down_left = count_steps(1, -1)  # ↙

    return down_right+up_left+up_right+down_left


def queensAttack(n, k, r_q, c_q, obstacles):
    number_of_rows = createRows(n, [r_q, c_q], obstacles)
    number_of_columns=createColumns(n, [r_q, c_q], obstacles)
    number_of_diagonals = createDiagonal(n, [r_q, c_q], obstacles)

    return number_of_columns+number_of_rows+number_of_diagonals

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

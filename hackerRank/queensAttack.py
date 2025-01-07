#!/bin/python3

import math
import os
import random
import re
import sys



def queen_moves_in_row(n, queen, obstacles):
    # Queen's position
    r_q, c_q = queen
    
    # Obstacles in the same row
    obstacles_in_row = [obs for obs in obstacles if obs[0] == r_q]
    
    # Initialize the steps the queen can take
    steps_left = c_q - 1  # Queen can move left until column 1
    steps_right = n - c_q  # Queen can move right until column n
    
    # Handle obstacles in the same row
    for obs in obstacles_in_row:
        c_obs = obs[1]  # Column of the obstacle
        if c_obs < c_q:  # Obstacle is to the left of the queen
            steps_left = min(steps_left, c_q - c_obs - 1)
        elif c_obs > c_q:  # Obstacle is to the right of the queen
            steps_right = min(steps_right, c_obs - c_q - 1)
    
    # Total valid moves in the row
    total_moves_in_row = steps_left + steps_right
    return total_moves_in_row

def queen_moves_in_column(n, queen, obstacles):
    # Queen's position
    r_q, c_q = queen
    
    # Obstacles in the same column
    obstacles_in_column = [obs for obs in obstacles if obs[1] == c_q]
    
    # Initialize the steps the queen can take
    steps_up = r_q - 1  # Queen can move up until row 1
    steps_down = n - r_q  # Queen can move down until row n
    
    # Handle obstacles in the same column
    for obs in obstacles_in_column:
        r_obs = obs[0]  # Row of the obstacle
        if r_obs < r_q:  # Obstacle is above the queen
            steps_up = min(steps_up, r_q - r_obs - 1)
        elif r_obs > r_q:  # Obstacle is below the queen
            steps_down = min(steps_down, r_obs - r_q - 1)
    
    # Total valid moves in the column
    total_moves_in_column = steps_up + steps_down
    return total_moves_in_column



def queen_moves_in_diagonals(n, queen, obstacles):
    # Queen's position
    r_q, c_q = queen
    
    # Obstacles on the four diagonals
    obstacles_on_diagonals = []
    for obs in obstacles:
        r_obs, c_obs = obs
        # Check if the obstacle is on any of the four diagonals
        if abs(r_obs - r_q) == abs(c_obs - c_q):  # If the difference between rows and columns is the same
            obstacles_on_diagonals.append(obs)

    # Function to count the number of valid moves in a diagonal direction
    def count_steps(di, dj):
        steps = 0
        x, y = r_q + di, c_q + dj
        closest_obstacle = None
        
        while 1 <= x <= n and 1 <= y <= n:  # Stay within bounds
            if [x, y] in obstacles_on_diagonals:  # Stop if an obstacle is encountered
                closest_obstacle = [x, y]
                break
            steps += 1
            x += di
            y += dj
        
        return steps

    # Calculate valid moves in each diagonal direction
    down_right = count_steps(1, 1)  # Down-right diagonal
    up_left = count_steps(-1, -1)   # Up-left diagonal
    up_right = count_steps(-1, 1)   # Up-right diagonal
    down_left = count_steps(1, -1)  # Down-left diagonal

    # Total valid moves in all four diagonals
    total_moves_in_diagonals = down_right + up_left + up_right + down_left
    return total_moves_in_diagonals

def queensAttack(n, k, r_q, c_q, obstacles):
    number_of_rows = queen_moves_in_row(n, [r_q, c_q], obstacles)
    number_of_columns=queen_moves_in_column(n, [r_q, c_q], obstacles)
    number_of_diagonals = queen_moves_in_diagonals(n, [r_q, c_q], obstacles)

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

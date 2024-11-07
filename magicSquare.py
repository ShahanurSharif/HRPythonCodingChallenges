#!/bin/python3

import math
import os
import random
import re
import sys

# Global list to store the cost of converting `s` to each possible magic square
sum_arr = []

# Function to calculate the "magic constant" for a square of given length
def magicNumber(length=0):
    total = length * (length * length + 1) / 2
    return int(total)

# Helper function to check if all elements in an array are equal
def is_equal(arr):
    return all(x == arr[0] for x in arr)

# Function to determine if a given 2D array `s` is a magic square
def is_magic_square(s):
    lrd = 0  # Sum of left-to-right diagonal
    rld = 0  # Sum of right-to-left diagonal
    sr = []  # Row sums
    sc = []  # Column sums
    row_total = len(s[0])  # Length of a row (assuming square matrix)

    # Calculate row sums, column sums, and diagonal sums
    for i in range(len(s)):
        lrd += s[i][i]
        rld += s[i][row_total - i - 1]
        sr.append(sum(s[i]))  # Row sum
        sc.append(sum(s[j][i] for j in range(len(s[i]))))  # Column sum

    # Check if all row sums, column sums, and diagonal sums are equal
    if is_equal(sr) and is_equal(sc):
        if lrd == sr[0] and rld == sr[0]:
            return True  # Valid magic square
    return False  # Not a magic square

# Recursive function to generate all permutations of a given list `arr`
def get_permutations(arr):
    if len(arr) == 1:
        return [arr]

    prem = []
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i + 1:]
        for p in get_permutations(remaining):
            prem.append([current] + p)
    return prem

# Function to calculate the cost of converting `s` to `value`
# The cost is the sum of absolute differences between corresponding elements
def nearest_match(value, s):
    total_sum = 0
    for j in range(len(s[0])):
        for k in range(len(s[0])):
            diff = abs(value[j][k] - s[j][k])
            total_sum += diff
    return total_sum

# Function to generate all possible magic squares based on `s` dimensions
# and store the minimum conversion cost in `sum_arr`
def generate_possible_magic_squares(s):
    length = len(s[0])  # Side length of the square matrix
    number_of_box = length * length + 1  # Total possible numbers in the square
    numbers = list(range(1, number_of_box))  # List of all possible numbers
    combinations = get_permutations(numbers)  # Generate all permutations
    total = [[] for _ in range(len(combinations))]  # Store all possible squares

    # Convert each permutation to a 2D matrix
    for i in range(len(combinations)):
        c = combinations[i]
        b = []
        for j in range(len(c)):
            b.append(c[j])
            if len(b) == length:
                total[i].append(b)
                b = []

    # Check if each generated matrix is a magic square
    for i in range(len(total)):
        if is_magic_square(total[i]):
            # If it's a magic square, calculate the conversion cost
            sum_arr.append(nearest_match(total[i], s))

# Main function to find the minimal conversion cost
def formingMagicSquare(s):
    generate_possible_magic_squares(s)
    if len(sum_arr) == 0:
        return 0  # No magic square found (edge case)
    else:
        return sorted(sum_arr)[0]  # Return the minimum conversion cost

# Example input for testing the function
if __name__ == '__main__':
    s = [[7, 2, 9], [6, 6, 2], [5, 1, 2]]
    result = formingMagicSquare(s)
    print(result)
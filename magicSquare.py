#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def magicNumber(length=0):
    total = length * (length * length + 1) / 2
    return int(total)


def is_equal(arr):
    val = arr[0]
    a = True
    for v in arr:
        print(val, v)
        if v != val:
            a=False
            break
    return a

def is_magic_square(s):
    lrd = 0
    rld = 0
    sr = []
    sc = []

    row_total = len(s[0])
    for i in range(len(s)):
        lrd += s[i][i]
        rld += s[i][row_total - i - 1]
        sr.append(sum(s[i]))
        sc.append(sum(s[i][j] for j in range(len(s[i]))))

    return is_equal(sr) and is_equal(sc) and lrd == rld

def get_permutations(arr):
    if len(arr) == 1:
        return [arr]

    prem = []
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for p in get_permutations(remaining):
            prem.append([current] + p)

    # print(prem)
    return prem

def generate_possible_magic_squares(s):
    length = len(s[0])
    # number_of_box = 4
    number_of_box = length*length + 1
    numbers = []
    for i in range(1, number_of_box):
        numbers.append(i)

    combinations = get_permutations(numbers)
    b = []
    total = [[] for _ in range(len(combinations))]
    for i in range(len(combinations)):
        c = combinations[i]
        for j in range(len(c)):
            b.append(c[j])
            if len(b) == length:
                total[i].append(b)
                b=[]

    possible_magic_squares = []
    for i in range(len(total)):
        if is_magic_square(total[i]):
            possible_magic_squares.append(total[i])

    return possible_magic_squares

def formingMagicSquare(s):
    length = len(s[0])
    magic_number = magicNumber(length)

    values = generate_possible_magic_squares(s)
    print(values)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

    result = formingMagicSquare(s)

    print(result)

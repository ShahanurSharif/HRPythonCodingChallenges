#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def doSearch(rank, score):
    low = 0
    high = len(rank) - 1
    while low<=high:
        guess = (low+high)//2
        # print(guess, low, high, guess, rank, score)
        if rank[guess] == score:
            return guess + 1
        elif rank[guess]<score:
            high = guess-1
        else:
            low = guess+1

    return low + 1


def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = sorted(set(ranked), reverse=True)
    result = []
    for score in player:
        # print(score)
        rank = doSearch(ranked, score)
        result.append(rank)

    return result


# 6
# 4
# 2
# 1
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # ranked_count = int(input().strip())

    # ranked = list(map(int, input().rstrip().split()))

    # player_count = int(input().strip())

    # player = list(map(int, input().rstrip().split()))

    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [5, 25, 50, 120]
    result = climbingLeaderboard(ranked, player)
    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()

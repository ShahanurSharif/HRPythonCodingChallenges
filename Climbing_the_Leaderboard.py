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
    # print(rank, score, low, high)
    while low<=high:
        guess = (low+high)//2
        print(low, high, rank, rank[guess], score)
        if rank[guess] == score:
            return guess + 1
        elif rank[guess]<score:
            low = guess+1
        else:
            high = guess-1

    return -1


def climbingLeaderboard(ranked, player):
    # Write your code here
    sort_score = []
    for score in sorted(player, reverse=True):
        new_rank = ranked[:]
        new_rank.append(score)
        new_rank = list(set(new_rank))
        new_rank = sorted(new_rank, reverse=True)
        value = doSearch(new_rank, score)
        if value:
            sort_score.append(value)

    return sorted(sort_score, reverse=True)


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

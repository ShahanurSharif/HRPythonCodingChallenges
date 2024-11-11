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

def climbingLeaderboard(ranked, player):
    # Write your code here
    merge_arr = ranked + player
    merge_arr = list(set(merge_arr))
    sorted_merge_arr = sorted(merge_arr, reverse=True)
    ranked_detail = []
    for board_score in player:
        for i in range(len(sorted_merge_arr)):
            if board_score == sorted_merge_arr[i]:
                ranked_detail.append(i + 1)

    print(sorted_merge_arr, player, ranked_detail)

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

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()

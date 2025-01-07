#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

class RecordTracker:
    def __init__(self, initial_score):
        self.higest_score = initial_score
        self.lowest_score = initial_score
        self.highest_record_break = 0
        self.lowest_record_break = 0


def breakingRecords(scores):
    # Write your code here
    tracker = RecordTracker(scores[0])


scores = [
    [10, 5, 20, 20, 4, 5, 2, 25, 1],
    [3, 4, 21, 36, 10, 28, 35, 5, 24, 42],
]
result = breakingRecords(scores[1])
print(result)
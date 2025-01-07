#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    # refund_amount = 0
    # [3, 10, 2, 9] 1 12
    total_bill = sum(bill)
    anna_items=bill[:]
    anna_items.pop(k)
    anna_bill = sum(anna_items) / 2
    refund_amount =int(b - anna_bill)
    # print(refund_amount, anna_bill)
        # anna_should_pay = sum(anna_items)
    if refund_amount == 0:
        print('Bon Appetit')
    else:
        print(refund_amount)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

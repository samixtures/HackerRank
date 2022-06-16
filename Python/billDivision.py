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
    
    #add all values excluding index k
    #subtract "b" by that sum and return the new value

    sum = 0
    for x in range(len(bill)):
        if x == k:
            continue
        sum += bill[x]
    res = int(b-(sum/2))
    if res == 0:
        print("Bon Appetit")
    else:
        print(res)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

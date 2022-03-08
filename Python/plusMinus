#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p_counter = 0
    n_counter = 0
    z_counter = 0
    total = len(arr)
    for x in arr:
        if x > 0:
            p_counter+=1
        elif x < 0: 
            n_counter+=1
        elif x == 0:
            z_counter +=1
    p_counter /= total
    n_counter /= total
    z_counter /= total
    print(p_counter)
    print(n_counter)
    print(z_counter)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

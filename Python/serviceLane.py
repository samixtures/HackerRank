#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n, cases):
    # Write your code here
    """
    n = 8 -> size of width?
    width = [2, 3, 1, 2, 3, 2, 3, 3] width along a lane on the highway
    cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
    
    Loop through cases, use splice notation to go through the indices given by the
    exit and entrance #s in cases and find the minimum. Append a list with that minimum.
    
    """
    res = []
    for i in range(len(cases)):
        start = cases[i][0]
        end = cases[i][1]
        minVal = float('inf')
        for j in range(start, end+1):
            minVal = min(minVal, width[j])
        res.append(minVal)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

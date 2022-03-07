#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0
    y = 0
    for x in range(len(arr)): # x goes from 0 to 3
        # print(arr[x][x])
        sum1+=arr[x][x]
    for x in range(len(arr)-1, -1, -1): # we need x to go from 3 to 0
       # print(arr[x][y])
        sum2+=arr[x][y] # actually we need the first [x] to be from 3 to 0, and the second from 0 to 3
        y+=1
    sum1 -= sum2
    return abs(sum1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min = arr[0]
    max = arr[0]
    sum = 0
    minRes, maxRes = None, None
    # alawys array of 5, meaning we always just have to loop times for x in range(5)
    # print two space-separated integers on line line: print(min, max)
    for x in arr:
        if min < x:
            min = x
    for x in arr:
        if max > x:
            max = x
    for x in arr:
        sum += x
    minRes = sum - min
    maxRes = sum - max
    print(minRes, maxRes)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

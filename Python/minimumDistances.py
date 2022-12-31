#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    
    """
    Was thinking set because of duplicates but sliding window also makes sense.
    Loop through, keep a pointer that starts off at 1 + x, keep counter, keep minim.
    Create second loop that checks for every index after x until we find same # or end.
    """
    # 3,2,1,2,3
    minim = float('inf')
    for x in range(len(a)):
        counter = 1
        point = x+1
        while point < len(a):
            if a[point] == a[x]:
                minim = min(minim, counter)
                break
            point += 1
            counter += 1
    if minim == float('inf'):
        return -1
    return minim
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

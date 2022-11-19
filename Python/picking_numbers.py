#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    h = {}
    max_count = 0
    for x in a:
        h[x] = 1 + h.get(x, 0)
    for x in h:
        max_count = max(h[x], max_count)
        if x+1 in h:
            max_count = max(h[x] + h[x+1], max_count)
        if x-1 in h:
            max_count = max(h[x] + h[x-1], max_count)
    return max_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

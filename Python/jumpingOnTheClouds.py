#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    # 000010
    # 0010010
    final = len(c)-1
    curr = 0
    jumps = 0
    while curr != final:
        if (curr < final-1) and c[curr+2] == 0:
            curr += 2
        else:
            curr += 1
        jumps += 1
    return jumps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

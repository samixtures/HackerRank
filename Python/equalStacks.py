#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    
    height1, height2, height3 = sum(h1), sum(h2), sum(h3)
    
    if height1 == height2 == height3: return height1
    
    while height1 > height3:
        h1Top = h1.pop(0)
        height1 -= h1Top
    
    while height1 > height2:
        h1Top = h1.pop(0)
        height1 -= h1Top
        
    while height2 > height1:
        h2Top = h2.pop(0)
        height2 -= h2Top
        
    while height3 > height1:
        h3Top = h3.pop(0)
        height3 -= h3Top
        
        
    return height1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

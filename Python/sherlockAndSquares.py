#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    squaresCounter = 0
    
    for i in range(a, b+1):
        print("i:", i)
        actualRoot = math.sqrt(i)
        decimalRemainder = math.sqrt(i) % 1
        print("decimalRemainder:", decimalRemainder)
        if decimalRemainder == 0:
            squaresCounter += 1
        nextRoot = (actualRoot+1) * (actualRoot+1)
        print("nextRoot:", nextRoot)
        if (nextRoot % 1 == 0) and nextRoot > b:
            break
    return squaresCounter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

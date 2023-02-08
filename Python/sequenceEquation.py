#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    # [5, 2, 1, 3, 4]
    #  1, 2, 3, 4, 5
    result = []
    for i in range(len(p)): # 0, 1, 2, 3, 4. 1, 2, 3, 4, 5
        # i = 0
        first = p.index(i+1) + 1 # p.index(0+1) -> 2 + 1 -> 3
        second = p.index(first) + 1 # p.index(3) -> 3 + 1 -> 4
        result.append(second)
    print(result)
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

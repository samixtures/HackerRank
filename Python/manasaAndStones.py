#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    """
        a = 1, b = 2, n = 2, 3, 4

        11, 12    a*2+b*0, a*1+b*1
        22, 21    b*2+a*0, b*1+a*1

        111, 112, 121, 211    a*3+b*0, a*2+b*1, a*2+b*1, a*2+b*1
        222, 221, 212, 122    b*3+a*0, b*2+a*1, b*2+a*1, b*2+a*1

        1111, 1112, 1121, 1211, 2111
        2222, 2221, 2212, 2122, 1222
        
        i and j have to add up to n, so we can just repalce j with n-i
    """
    # Write your code here
    i, j = n-1, 0
    num_set = set()
    res = []
    while i >= 0:
        val = a*i+b*((n-1)-i)
        print("val is", val)
        if val not in num_set:
            num_set.add(val)
            res.append(val)
        i-=1
    res.sort()
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

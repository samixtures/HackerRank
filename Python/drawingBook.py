#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if p > 1 and p % 2 == 0:
        p += 1
    if n > 1 and n % 2 == 0:
        n += 1
    print("p is", p)
    print("n is", n)
    if n - p == 0:
        print("they become zero")
        return 0
    start_turn = (p - 1)/2
    end_turn = (n - p)/2
    res = int(min(start_turn, end_turn))
    print(res)
    return res
    
    # p = 2 -> 3
    # 1 - 3 -> 2/2 = 1
    # 1 - 5 -> 4/2 = 2
    
    # n = 6
    # p = 3
    # 6 - 3 = 3/2 -> 
    
    # 3 - 1 = 4/2
    # 6 - 2 = 4 / 2 = 2
    # 7 - 2 = int(5 / 2) = 2
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

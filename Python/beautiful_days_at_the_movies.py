#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    def reverse(n):
        # to reverse, i'm thinking of using a stack
        # eh actually if we do % 10
        # 23 % 10 == 3
        # 2 % 10 == 2
        # so we mod 10, and save the remainder somewhere
        # a queue seems more appropriate
        q = []
        ret = 0
        while n != 0:
            q.append(n%10)
            n = n//10
        while q:
            temp = q.pop(0)
            ret *= 10
            ret += temp

        return ret
    # create counter variable, keeping track of beautiful days
    # loop from i to k using the variable x
    # have an if statement checking if (x - reverse(x)) % k == 0
    # if so increment a counter variable
    # return that counter variable
    
    counter = 0
    for x in range(i, j+1):
        if (x - reverse(x)) % k == 0:
            counter += 1
    return counter
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

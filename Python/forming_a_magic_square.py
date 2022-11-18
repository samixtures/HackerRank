#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    num_set = set()
    duplic = set()
    cost = 0
    
    # check for duplicates
    for x in s:
        for y in x:
            if y in num_set:
                duplic.add(y)
            else: num_set.add(y)

    # check if each row adds up to 15
    for x in s:
        # if it doesn't, check if there's a number in the duplicates
        if sum(x) != 15:
            for y in x:
                # if there's a duplic, find what it would need to change to for the sum to be 15
                if y in duplic:
                    print("duplic val is ", y)
                    print("the array is", x)
                    print("sum is", sum(x))
                    new_val = abs(15-(sum(x)-y))
                    print("the change is", new_val)
                    cost += abs(new_val-y)
                    duplic.remove(y)
                    y = new_val
                    duplic.add(y)
            
    return cost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

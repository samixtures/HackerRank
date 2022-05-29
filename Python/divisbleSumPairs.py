#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    # nested for loops: x stays at one element, y checks all other
    # elements that are of a greater index than x, and if adding them together
    # produces a value % 5 == 0, then increase counter
    
    # can also use a dictionary?
    # check if a value is in the dictionary initially, if it's not then
    # add it
    
    # if it is in the dictionary, then check if the key is greater than the current index
    # if it is then check if the value plus the current index's value
    # mod 5 is == 0
    counter = 0
    for i, x in enumerate(ar[::]):
        for j, y in enumerate(ar[1::]):
            print(x, y)
            if j+1 > i and (x + y) % k == 0: 
                counter += 1
    return counter
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

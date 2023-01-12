#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    # $15, $3 per bar, 2 wrappers = a bar (of chocolate)
    #   n,  c,         m
    '''
    15//3 = 5 total bars = 5 wrappers
    5%2 = 1 remaining wrapper after cashing in wrappers
    5//2 = 2 more bars from wrappers
    1 + 2 = 3 wrappers in total now
    3%3 = 0 remaining wrappers after cashing in wrappers
    3//3 = 1 more bar from wrappers
    1%3 = 1 remaining wrapper after cashing in wrappers
    1//3 = 0 more bars from wrappers
    END
    
    '''
    totalBars = 0
    money = n
    moneyPerBar = c
    wrappersPerBar = m
    totalWrappers = 0
    
    totalBars += money // moneyPerBar
    totalWrappers += totalBars
    
    while True:
        remainingWrappers = totalWrappers % wrappersPerBar
        totalBars += totalWrappers // wrappersPerBar
        totalWrappers = totalWrappers // wrappersPerBar + remainingWrappers
        
        if totalWrappers // wrappersPerBar == 0:
            break
    return totalBars
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()

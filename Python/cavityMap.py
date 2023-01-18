#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    counter = 0
    for x in grid:
        for i in range(len(x)):
            if i > 0 and i < len(x)-1:
                if int(x[i]) > int(x[i-1]) and int(x[i]) > int(x[i+1]):
                    for j in range(len(x)):
                        temp = x[0:i] + "X" + x[i+1:]
                        grid[counter] = temp
        counter += 1
    return grid
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    below_sea_level = False
    is_sea_level = True
    track_steps = 0
    counter = 0
    for i in range(len(path)):
        if path[i] == 'U':
            track_steps += 1
        elif path[i] == 'D':
            track_steps -= 1
        if track_steps != 0:
            is_sea_level = False
        elif track_steps == 0:
            is_sea_level = True
        if track_steps < 0:
            below_sea_level = True
        if below_sea_level == True and is_sea_level == True:
            counter += 1
            below_sea_level = False
        print(track_steps)
    return counter
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

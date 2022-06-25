#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    
    #first # is her original score
    #create 2 counters -> high, low
    #if she gets a value higher than origin
    #high += 1 and max = current index
    #same with with a value lower than the origin
    #return [high, low]

    max, min = scores[0], scores[0]
    high, low = 0, 0
    for x in scores:
        if x > max:
            high += 1
            max = x
        elif x < min:
            low += 1
            min = x
    return[high, low]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

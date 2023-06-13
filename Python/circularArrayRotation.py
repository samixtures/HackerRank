#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    
    # (current pos + k) % len(a)
    
    finalPositionsDict = {}
    
    for i in range(len(a)):
        finalPosition = (i + k) % len(a)
        
        finalPositionsDict[finalPosition] = a[i]
        
        """
        finalPositionsDict = {2: 1, 0: 2, 1: 3}
        
        for i in range(len(a)):
            returnList.append(finalPositionsDict[i])
            
        returnList = [2, 3, 1]
        """
        
    
    returnList = []
    
    for i in range(len(a)):
        returnList.append(finalPositionsDict[i])
    
    finalList = []
    
    for x in queries:
        finalList.append(returnList[x])
        
    return finalList

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

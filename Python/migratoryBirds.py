#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    
    # create an array
    # go through arr, use a counter to determine
    # the max # of times any bird is sited
    
    # afterwards, go through the array again and 
    # if an id has been spotted that many times then
    # add it to the array
    # then return the min of this array

    site = []
    counter = 0
    
    #scratch that; let's make a frequency map
    
    h = {}
    
    for x in arr[::]:
        if x in h:
            h[x] += 1
        else:
            h[x] = 1
    # now we have a map that has the number 
    # each number occurs. To get the max I think we can
    # just do a for loop?
    max = 0
    maxIndex = 0
    for x in h:
        if h[x] > max:
            max = h[x]
            maxIndex = x
    for x in h:
        if max == h[x]:
            site.append(x)
    print(h)
    print(site)
    
    return min(site)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

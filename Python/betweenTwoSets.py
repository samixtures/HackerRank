#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    
    def fact(x): # returns list of factors of any value
        l = []
        for i in range(1, x+1):
            if x % i == 0:
                l.append(i)
        return(l)
        
    def all_list_values(j, k): # True if all values in list j are in list k
        for x in j:
            if x not in k:
                return False
        return True
    
    res = []
    for i in range(len(b)):
        considered_list = fact(b[i])
        for x in considered_list:
            if all_list_values(a, fact(x)):
                res.append(x)
    print("res is", res)
    h = {}
    for x in res:
        if x not in h:
            h[x] = 1
        else:
            h[x] += 1
    counter = 0
    for x in h:
        if h[x] == len(b):
            counter += 1
    return counter
        
    
    #FORGET ALL THIS
    # set a variable = to the max of the first array
    # while curr <= 
    
    # we could just check all values less than or equal to max(b)
    # there's likely a better way of doing it
    # we could narrow it down only to numbers that are a multiple of 
    # the minimum of a
    # temp = None
    # for c in range(max(a), max(b)+max(a), max(a)):
    #     if c % 
    #     print(c)
    
    # counter = 0
    # maxVal = max(b)
    # minVal = min(a)
    # for x in range(maxVal):
    #     for y in a:
    #         if x % y == 0:
    #             for z in b:
    #                 if x != 0 and z % x == 0:
    #                     counter +=1
    #                 else:
    #                     continue
    #         else:
    #             continue
    # return counter
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

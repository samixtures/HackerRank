#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def printList(l):
    for x in l:
        print(x, end=' ')
def insertionSort1(n, arr):
    # Write your code here
    # go from back to start
    # compare stored value to current indexed value
    # if store < arr[x]: arr[x+1] = arr[x]
    # [1, 2, 4, 5, 3]
    # elif store > arr[x]: arr[x+1] = store 
    
    val = arr[-1]
    i = len(arr)-1 # 3
    inside = False
    for x in arr[::-1]:
        if val < x: # 3 > 8
            arr[i+1] = x
        elif val > x: 
            arr[i+1] = val
            inside = True
            break
        if i < len(arr)-1:
            printList(arr)
            print("")
        i-=1
    if inside == False:
        arr[0] = val
    printList(arr)
    
    # store = arr[len(arr)-1]
    # for x in range(len(arr)-2, -1, -1): # 2 4 6 8 3
    #     if store < arr[x]: # 3 < 4
    #         arr[x+1] = arr[x] # 2 4 4 6 8
    #     elif store > arr[x]: # 3 > 2
    #         arr[x+1] = store # 2 3 4 6 8
    #         break
    #     printList(arr)
    #     print("")
    # printList(arr)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

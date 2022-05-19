#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    #s = start, t = end
    #a = apple tree, b = orange tree
    #apples and oranges are lists with
    #the same # of indices as a and b, each with a #
    #denoting how far the specific index fruit falls
    
    #create a loop size of the lists
    #   add each value at the same indices of 
    #   a to the values of apples, and b to oranges
    for x in range(len(apples)):
        apples[x]+=a
    for x in range(len(oranges)):
        oranges[x]+=b
        #^ this should tell us where each fruit landed
    #create another loop size of lists that checks if
    # if s <= a <= t: countA+=1
    # if s <= b <= t: countB+=1
    countA = 0
    countB = 0
    for x in range(len(apples)):
        if s <= apples[x] <= t: 
            countA+=1
    for x in range(len(oranges)):
        if s <= oranges[x] <= t: 
            countB+=1
    print(countA)
    print(countB)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

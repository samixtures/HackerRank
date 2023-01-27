#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here

    counter = 0
    numbOfMessages = int(len(s)/3)
    correctStr = ""
    for x in range(numbOfMessages):
        correctStr += "SOS"
    for i in range(len(s)):
        if s[i] != correctStr[i]:
            counter += 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # get the second last value of the string and check if it's A or P -> s[-2]
    # if s[-2] == 'A'
    #  return s[:-2:]
    # if s[-2] == 'P'
    # hour = int(s[:3:]) # gives us the hours
    # hour = 12 - hour
    # return hour+s[2:-2:]
    if s[-2] == 'A':
        hour = int(s[:2:])
        if hour == 12:
            hour = 12-hour
            return '0'+str(hour)+s[2:-2:]
        return s[:-2:]
    elif s[-2] == 'P':
        hour = int(s[:2:])
        if hour == 12:
            return s[:-2:]
        hour = 12+hour
        return str(hour)+s[2:-2:]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

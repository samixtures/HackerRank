#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    
    # Problem: Get the hours and minutes in actual words
    str = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten",
                "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen","eighteen", "nineteen","twenty",
                "twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty six","twenty seven","twenty nine","half" ]
    
    # ${h} o' clock
    if m == 0:
        return f"{str[h-1]} o' clock"
    if m == 1:
        return f"{str[m-1]} minute past {str[h-1]}"
    # ${m} minute past ${h}
    if m == 15:
        return f"quarter past {str[h-1]}"
    if m == 30:
        return f"half past {str[h-1]}"
    if m < 30 and m > 0:
        return f"{str[m-1]} minutes past {str[h-1]}"
    # ${60-m} minutes to ${h+1}
    if m == 45:
        return f"quarter to {str[h]}"
    if m > 30:
        return f"{str[60-m-1]} minutes to {str[h]}"
        pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

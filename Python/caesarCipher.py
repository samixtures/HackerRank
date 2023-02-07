#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    letters = "abcdefghijklmnopqrstuvwxyz"
    lettersUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret_str = ""
    for x in s:
        if x in letters:
            if letters.index(x)+k < 26:
                ret_str += letters[letters.index(x)+k]
            else:
                ret_str += letters[letters.index(x)+k-26]
        elif x in lettersUp:
            if lettersUp.index(x)+k < 26:
                ret_str += lettersUp[lettersUp.index(x)+k]
            else:
                ret_str += lettersUp[lettersUp.index(x)+k-26]
        else: 
            ret_str += "-"
    return ret_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    list = []
    while n > 0:
        remainder = n%2
        list.append(remainder)
        n = int(n/2)
    # print(list)
    counter = 0
    max_counter = 0
    for x in list:
        if x == 1:
            counter+=1
        elif x == 0:
            counter = 0
        if counter > max_counter:
                max_counter = counter
    print(max_counter)
        
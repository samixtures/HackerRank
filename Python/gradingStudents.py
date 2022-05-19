#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    #if grade > 37
    #add to the grade once and check if test % 5 == 0
    #add to the grade again and check if test % 5 == 0
    #if yes in either one then set grade = curr
    result = []
    for x in grades:
        grade = x
        if grade > 37:
            if (grade+1) % 5 == 0:
                grade+=1
            if (grade+2) % 5 == 0:
                grade+=2
        result.append(grade)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

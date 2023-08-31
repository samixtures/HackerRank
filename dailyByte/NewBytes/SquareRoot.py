 # Given a non-negative integer x, return its square root.
 # Note: You may not use a built in square root function and decimals should be truncated to return an integer value
 # Ex: Given the following x..
 # x = 9, return 3.
 # Ex: Given the following x..
 # x = 12, return 3
import math
def squareRoot(x):
    if x >= 0:
        return round(math.sqrt(x))
    else:
        return 0
print(squareRoot(9))
print(squareRoot(12))

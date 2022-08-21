# This question is asked by Google. Given an array of integers, return whether or not two numbers sum to a given target, k.
# Note: you may not sum a number with itself.

# Ex: Given the following...

# [1, 3, 8, 2], k = 10, return true (8 + 2)
# [3, 9, 13, 7], k = 8, return false
# [4, 2, 6, 5, 2], k = 4, return true (2 + 2)




test = [1, 3, 8, 2]
test1 = [4, 2, 6, 5, 2]
test2 = [3, 9, 13, 7]
k = 10
k1 = 4
k2 = 8
h = {}
def twoSum(test, k):
    for i, x in enumerate(test):
        print(x)
        print(h)
        if k - x in h:
            return True
        else:
            h[x] = i
    return False
print(twoSum(test2, k2))

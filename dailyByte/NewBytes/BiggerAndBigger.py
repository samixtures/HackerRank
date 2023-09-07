# Given an integer array, nums, return a list containing all subsets 
# of nums that contain at least two elements and have an increasing sequence.

# Ex: Given the following nums…

# nums = [1, 2, 3], return [[1,2],[1,2,3],[1,3],[2,3]].
# Ex: Given the following nums…

# nums = [2, 4, 3, 5], return [[2,4],[2,4,5],[2,3],[2,3,5],[2,5],[4,5],[3,5]].

import copy


def biggerAndBigger(arr):
    arr.sort()
    ret = []
    i = 0
    j = 1

    while j < len(arr):
        temp = []
        temp.append(arr[i])
        temp.append(arr[j])
        j += 1
        ret.append(temp)

    k = i
    j = i + 2

    temp = []
    while k <= j:
        temp.append(arr[k])
        k += 1

    ret.append(temp)

    print(ret)

biggerAndBigger([1, 2, 3])
biggerAndBigger([2, 4, 3, 5])

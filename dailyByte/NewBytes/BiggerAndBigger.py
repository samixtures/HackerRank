# Given an integer array, nums, return a list containing all subsets 
# of nums that contain at least two elements and have an increasing sequence.

# Ex: Given the following nums…

# nums = [1, 2, 3], return [[1,2],[1,2,3],[1,3],[2,3]].
# Ex: Given the following nums…

# nums = [2, 4, 3, 5], return [[2,4],[2,4,5],[2,3],[2,3,5],[2,5],[4,5],[3,5]].

def biggerAndBigger(arr):
    arr.sort()
    ret = []
    for i in range(len(arr)):
        j = i+1
        currentArr = [arr[i]]
        while j < len(arr):
            currentArr.append(arr[j])
            print("currArr", currentArr)
            ret.append(currentArr)
            print("ret:", ret)
            j += 1
    print(ret)

biggerAndBigger([1, 2, 3])

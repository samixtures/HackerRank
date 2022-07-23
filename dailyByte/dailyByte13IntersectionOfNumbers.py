# This question is asked by Google. Given two integer arrays, return their intersection.
# Note: the intersection is the set of elements that are common to both arrays.

# Ex: Given the following arrays...

# nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
# nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
# nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []

nums1, nums2 = [2, 4, 4, 2], [2, 4]
nums3, nums4 = [1, 2, 3, 3], [3, 3]
nums5, nums6 = [2, 4, 6, 8], [1, 3, 5, 7]
def intersection_of_numbers(n1, n2):
    res = []
    for x in n1:
        if x in n2 and x not in res:
            res.append(x)
    return res
print(intersection_of_numbers(nums5, nums6))
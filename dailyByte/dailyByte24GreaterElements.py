# This question is asked by Amazon. Given two arrays of numbers, 
# where the first array is a subset of the second array, return an array containing 
# all the next greater elements for each element in the first array, in the second array. 
# If there is no greater element for any element, output -1 for that number.

# Ex: Given the following arrays…

# nums1 = [4,1,2], nums2 = [1,3,4,2], return [-1, 3, -1] because no element in nums2 is greater than 4, 3 is the first number in nums2 greater than 1, and no element in nums2 is greater than 2.
# nums1 = [2,4], nums2 = [1,2,3,4], return [3, -1] because 3 is the first greater element that occurs in nums2 after 2 and no element is greater than 4.

nums1, nums2, nums3, nums4 = [4,1,2], [1,3,4,2], [2,4], [1,2,3,4]

def greater_elements(n1, n2):
    greater_list = []
    greater = False
    for x in n1:
        for y in n2:
            if y > x:
                greater_list.append(y)
                greater = True
                break
        if not greater:
            greater_list.append(-1)
        greater = False
    print(greater_list)

greater_elements(nums1, nums2)

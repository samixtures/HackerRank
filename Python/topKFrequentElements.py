
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hashMap = {}
    for x in nums: # 1
        if x in hashMap:
            hashMap[x] +=1
        else:
            hashMap[x] = 1 # 1
            
    max = 0
    maxList = []
    # 1:3, 2:2, 3:1
    # 3:1, 0:2, 1:1
    # loop through and get the max and add it to the list
    while k > 0:
        for x in hashMap:
            if x in maxList:
                continue
            print("hashMap[x]:", hashMap[x], "\n")
            print(type(x))
            if hashMap[x] > max:
                max = x          
            # print("x:", x)
            # print("hashMap[x]:", hashMap[x], "\n")
        maxList.append(max)
        k -= 1
        max = 0
    return maxList
testList = [1,1,1,2,2,3]
testK = 2
answerList = topKFrequent(testList, testK)
print("answer:", answerList)
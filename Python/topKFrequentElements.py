
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
            
    maxVal = 0
    maxKey = 0
    maxList = []
    # 1:3, 2:2, 3:1
    # loop through and get the max and add it to the list
    while k > 0:
        for x in hashMap:
            if x in maxList:
                continue
            if maxVal < hashMap[x]:
                maxVal = hashMap[x]
                maxKey = x
        maxList.append(maxKey)
        k -= 1
        maxVal = 0
    return maxList
testList = [1,1,2,2,2,3]
testK = 2
answerList = topKFrequent(testList, testK)
print("answer:", answerList)
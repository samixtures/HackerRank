class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for x in range(0, len(numbers), 1):
            compl = target-numbers[x]
            left = 0
            right = len(numbers)-1
            while left <= right:
                mid = (left+right)/2
                if numbers[mid] < compl:
                    left = mid+1
                if numbers[mid] > compl:
                    right = mid-1
                elif numbers[mid] == compl and mid == x:
                    return[x+1, mid+2]
                elif numbers[mid] == compl and mid != x:
                    return [x+1, mid+1]
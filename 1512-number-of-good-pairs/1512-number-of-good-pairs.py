class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] +=1 
            else:
                count[nums[i]] = 1
        pairs = 0
        for i in count:
            k = count[i]
            pairs = pairs + (k * (k-1)) // 2
        return pairs
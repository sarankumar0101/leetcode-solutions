class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sr = []
        nums.sort()
        for i in nums:
            sr.append(i*i)
        sr.sort()
        return sr

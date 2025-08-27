class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = set()
        twice = []
        for num in nums:
            if num not in arr:
                arr.add(num)
            else:
                twice.append(num)
        else:
            return twice
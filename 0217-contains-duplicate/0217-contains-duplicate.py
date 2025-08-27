class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = set()
        for num in nums:
            if num not in arr:
                arr.add(num)
            else:
                return True
                break
        return False
        
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = sorted(nums1+nums2)
        med = 0
        n = len(num)
        if n%2 == 0:
            med = (num[n//2 - 1] + num[n//2]) / 2.0
            return med
        else:
            med = num[n//2]
            return med
        
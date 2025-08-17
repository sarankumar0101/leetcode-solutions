class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        ry = y[::-1]
        if y == ry:
            return True
        else:
            return False
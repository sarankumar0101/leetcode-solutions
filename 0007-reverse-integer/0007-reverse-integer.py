class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x!=0:
            pop = x%10
            x = x//10
            rev = rev*10+pop
        rev = sign*rev
        if rev<-2**31 or rev>(2**31) - 1:
            return 0
        else:
            return rev
        

        
        
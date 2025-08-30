class Solution(object):
    def productExceptSelf(self, nums):
        lp =1
        rp =1
        res = []
        for i in range(len(nums)):
            res.append(lp)
            lp = lp * nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*rp
            rp = rp *nums[i]
        return res        
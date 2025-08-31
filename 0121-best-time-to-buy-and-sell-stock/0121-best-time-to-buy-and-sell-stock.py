class Solution(object):
    def maxProfit(self, prices):
        minval = prices[0]
        ans = 0
        for i in range(len(prices)):
            minval = min(prices[i],minval)
            profit = prices[i]-minval
            ans = max(ans,profit)
        return ans

        
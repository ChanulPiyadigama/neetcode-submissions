class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            made = prices[r] - prices[l]
            if made < 0:
                l = r
                r+=1
            else:
                r+=1
                maxProfit = max(made, maxProfit)
        return maxProfit
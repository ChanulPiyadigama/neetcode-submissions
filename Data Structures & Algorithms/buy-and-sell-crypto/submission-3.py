class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        profit = 0

        b = 0

        for s in range(1, len(prices)):
            r = prices[s] - prices[b]

            if r > profit:
                profit = r
            
            if prices[s] < prices[b]:
                b = s
        return profit

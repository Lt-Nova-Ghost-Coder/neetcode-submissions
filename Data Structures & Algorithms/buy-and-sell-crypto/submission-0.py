class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        maxProfit = 0
        minBuy = self.prices[0]
        for i in prices:
            maxProfit = max(maxProfit, i - minBuy)
            minBuy = min(minBuy, i)
        return maxProfit
        
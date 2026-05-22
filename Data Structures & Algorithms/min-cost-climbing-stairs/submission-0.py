class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        n = len(self.cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + self.cost[i - 1], dp[i - 2] + self.cost[i - 2])
        
        return dp[n]
        
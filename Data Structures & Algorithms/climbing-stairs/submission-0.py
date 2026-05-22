class Solution:
    def climbStairs(self, n: int) -> int:
        self.n = n
        if self.n <= 2:
            return n
        
        dp = [0] * (self.n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, self.n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[self.n]


        
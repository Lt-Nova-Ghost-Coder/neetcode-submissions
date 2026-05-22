class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        if not self.nums:
            return 0
        if len(self.nums) == 1:
            return self.nums[0]
        n = len(self.nums)
        dp = [0] * (n)
        dp[0] = self.nums[0]
        dp[1] = max(self.nums[0], self.nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], self.nums[i] + dp[i - 2])

        return dp[-1] 
        
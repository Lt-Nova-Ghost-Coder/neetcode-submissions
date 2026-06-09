class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        n = len(self.nums)
        dp = [False] * n
        dp[-1] = True

        for i in range(n - 2, -1, -1):
            end = min(n, i + self.nums[i] + 1)
            for j in range(i + 1, end):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]
        
        
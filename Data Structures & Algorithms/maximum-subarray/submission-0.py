class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.nums = nums
        first = self.nums[0]
        maxSum = first
        for i in range(1, len(self.nums)):
            second = max(self.nums[i] + first, self.nums[i])
            maxSum = max(maxSum, second)
            first = second
        
        return max(maxSum, first)
        
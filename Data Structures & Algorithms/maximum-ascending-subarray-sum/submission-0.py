class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        self.nums = nums

        maxSum = self.nums[0]
        Sum = self.nums[0]
        for i in range(1, len(self.nums)):
            if self.nums[i] > self.nums[i - 1]:
                Sum += self.nums[i]
            else:
                maxSum = max(maxSum, Sum)
                Sum = self.nums[i]
        
        return max(maxSum, Sum)

        
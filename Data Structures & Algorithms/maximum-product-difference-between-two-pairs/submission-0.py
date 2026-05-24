class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        self.nums = nums
        self.nums.sort()
        a = self.nums[-1]
        b = self.nums[-2]
        c = self.nums[0]
        d = self.nums[1]
        return ((a * b) - (c * d))
        
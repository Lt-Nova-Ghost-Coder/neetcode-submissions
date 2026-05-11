class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.nums = nums
        n = len(self.nums)
        for i in range(n):
            self.nums.append(self.nums[i])
        return self.nums
        
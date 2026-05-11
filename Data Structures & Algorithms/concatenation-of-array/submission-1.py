class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.nums = nums
        n = len(self.nums)
        ans = [0] * (2 * n)
        index = 0
        for i in range(len(self.nums)):
            ans[index] = self.nums[i]
            index += 1
        for i in range(len(self.nums)):
            ans[index] = self.nums[i]
            index += 1
        return ans
        
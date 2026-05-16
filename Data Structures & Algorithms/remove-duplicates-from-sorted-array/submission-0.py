class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        self.nums = nums
        l = 1
        for i in range(1, len(self.nums)):
            if self.nums[i] != self.nums[i - 1]:
                self.nums[l] = self.nums[i]
                l += 1
        return l
        
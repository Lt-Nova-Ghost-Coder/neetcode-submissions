class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums
        self.nums.sort()
        for i in range(1, len(self.nums)):
            if self.nums[i] == self.nums[i - 1]:
                return True
            else:
                continue
        return False
        
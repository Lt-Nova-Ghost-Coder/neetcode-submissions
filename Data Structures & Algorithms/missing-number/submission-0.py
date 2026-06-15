class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        self.nums = nums
        self.nums.sort()

        for i in range(len(self.nums)):
            if self.nums[i] != i:
                return i
            else:
                continue
        return len(self.nums)
        
        
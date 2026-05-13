class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] > self.nums[j]:
                    self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                else:
                    continue
        

        
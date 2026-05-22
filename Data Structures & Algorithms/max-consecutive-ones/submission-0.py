class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        self.nums = nums
        length = 0
        maxLength = 0
        for i in range(len(self.nums)):
            if self.nums[i] == 1:
                length += 1
            else:
                maxLength = max(maxLength, length)
                length = 0
        
        return max(maxLength, length)

        
        
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        self.nums = nums
        leftSum = 0
        rightSum = 0

        for i in range(len(self.nums)):
            pivot = i
            for j in range(pivot):
                leftSum += self.nums[j]
            for k in range(pivot + 1, len(self.nums)):
                rightSum += self.nums[k]
            
            if leftSum == rightSum:
                return i
            leftSum = rightSum = 0
        
        return -1
        
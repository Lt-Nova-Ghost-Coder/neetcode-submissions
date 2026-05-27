class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        self.nums = nums
        leftSum = 0
        totalSum = 0
        for i in self.nums:
            totalSum += i
        
        for i in range(len(self.nums)):
            rightSum = totalSum - leftSum - self.nums[i]
            if leftSum == rightSum:
                return i
            else:
                 leftSum += self.nums[i]
        return -1
        
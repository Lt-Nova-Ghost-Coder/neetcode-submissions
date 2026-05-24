class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        self.nums = nums
        increasingFlag = False
        decreasingFlag = False

        for i in range(1, len(self.nums)):
            if self.nums[i] >= self.nums[i - 1]:
                increasingFlag = True
            else:
                increasingFlag = False
                break
        for i in range(1, len(self.nums)):
            if self.nums[i] <= self.nums[i - 1]:
                decreasingFlag = True
            else:
                decreasingFlag = False
                break
        
        return (increasingFlag or decreasingFlag)



        
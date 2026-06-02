class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        self.nums = nums
        ans = 0
        for i in self.nums:
            ans = ans ^ i
        
        return ans
        
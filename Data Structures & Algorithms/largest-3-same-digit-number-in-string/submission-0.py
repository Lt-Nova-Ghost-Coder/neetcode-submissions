class Solution:
    def largestGoodInteger(self, num: str) -> str:
        self.nums = num
        maxNum = -1
        for i in range(len(self.nums) - 2):
            if self.nums[i] == self.nums[i + 1] == self.nums[i + 2]:
                maxNum = max(maxNum, int(self.nums[i]))
        if maxNum == -1:
            return ""
        else:
            return str(maxNum) * 3
        
        
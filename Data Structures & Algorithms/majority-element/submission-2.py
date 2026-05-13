class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        self.nums = nums
        num = self.nums[0]
        freq = 1
        for i in range(1, len(self.nums)):
            if self.nums[i] == num:
                freq += 1
            else:
                if freq == 0:
                    num = self.nums[i]
                    freq += 1
                else:
                    freq -= 1
        return num

        
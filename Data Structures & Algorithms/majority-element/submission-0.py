class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        self.nums = nums
        freq = 0
        val = self.nums[0]
        for i in range(len(self.nums)):
            if i == 0:
                val = self.nums[i]
                freq += 1
            if self.nums[i] == val:
                freq += 1
            else:
                if freq == 0:
                    val = self.nums[i]
                    freq = 1
                else:
                    freq -= 1
        return val
        
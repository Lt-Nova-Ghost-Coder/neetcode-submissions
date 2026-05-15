class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        self.nums = nums
        seen = set(self.nums)
        for i in range(1, 2**31):
            if i not in seen:
                return i
            else:
                continue
        return -1
        
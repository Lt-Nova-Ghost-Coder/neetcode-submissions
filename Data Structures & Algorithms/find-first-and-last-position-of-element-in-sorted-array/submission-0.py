class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        start = -1
        end = -1
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if start == -1:
                    start = i
                else:
                    end = i
            else:
                continue
        if start == -1 and end == -1:
            return [-1, -1]
        if start != -1 and end == -1:
            return [start, start]
        else:
            return [start, end]
        
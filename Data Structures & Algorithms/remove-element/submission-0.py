class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        self.nums = nums
        self.val = val
        k = 0
        for i in range(len(self.nums)):
            if self.nums[i] != self.val:
                self.nums[k] = self.nums[i]
                k += 1
            else:
                continue
        return k
        
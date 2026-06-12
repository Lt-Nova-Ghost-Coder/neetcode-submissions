class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target

        res = len(self.nums)
        l = 0
        r = res - 1

        while l <= r:
            mid = l + (r - l) // 2
            if self.nums[mid] == self.target:
                return mid
            if self.nums[mid] > self.target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums
        seen = set()
        for i in self.nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False

        
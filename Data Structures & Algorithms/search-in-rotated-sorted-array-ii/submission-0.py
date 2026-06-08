class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        self.nums = nums
        self.target = target
        seen = set(self.nums)
        if self.target in seen:
            return True
        return False
        
        
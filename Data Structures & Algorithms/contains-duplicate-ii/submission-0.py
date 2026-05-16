class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        self.nums = nums
        self.k = k
        charIndex = {}
        for i in range(len(self.nums)):
            if self.nums[i] not in charIndex:
                charIndex[self.nums[i]] = i
            else:
                if abs(i - charIndex[self.nums[i]]) <= self.k:
                    return True
                else:
                    charIndex[self.nums[i]] = i
        return False

        
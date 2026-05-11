class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        self.nums = nums
        n = len(self.nums)
        seen = set()
        for i in self.nums:
            seen.add(i)
        ans = []
        for i in range(1, n + 1):
            if i not in seen:
                ans.append(i)
            else:
                continue
        return ans
            
        
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        self.nums = nums
        numbers = set(self.nums)

        n = len(self.nums)
        ans = []
        for i in range(1, n + 1):
            if i not in numbers:
                ans.append(i)
            else:
                continue
        return ans

        

            
        
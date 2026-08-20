class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums = nums
        self.target = target

        res = []
        def backtrack(i, curr, total):
            if total == self.target:
                res.append(curr.copy())
                return 
            
            if i == len(self.nums) or total > self.target:
                return 
            
            curr.append(self.nums[i])
            backtrack(i, curr, total + self.nums[i])

            curr.pop()

            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)

        return res
            
        
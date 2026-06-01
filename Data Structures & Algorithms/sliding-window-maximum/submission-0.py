class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        self.nums = nums
        self.k = k
        q = deque([])
        res = []
        for i in range(self.k):
            q.append(self.nums[i])
        
        res.append(max(q))
        for i in range(self.k, len(self.nums)):
            q.popleft()
            q.append(self.nums[i])
            res.append(max(q))
        return res

        
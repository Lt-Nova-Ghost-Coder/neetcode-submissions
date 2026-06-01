class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import heapq
        self.nums = nums
        heapq.heapify(self.nums)
        res = []
        while self.nums:
            res.append(heapq.heappop(self.nums))
        
        return res
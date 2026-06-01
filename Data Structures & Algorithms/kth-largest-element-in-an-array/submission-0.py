class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        self.nums = nums
        self.k = k
        minHeap = self.nums
        heapq.heapify(minHeap)
        while len(minHeap) > self.k:
            heapq.heappop(minHeap)
        
        return minHeap[0]
        
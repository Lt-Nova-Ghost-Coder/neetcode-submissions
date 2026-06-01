class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq
        self.gifts = gifts
        self.k = k
        minHeap = [self.gifts[i] * -1 for i in range(len(self.gifts))]
        heapq.heapify(minHeap)
        
        while self.k != 0:
            maxPile = -heapq.heappop(minHeap)
            floor = int(maxPile ** (0.5))
            heapq.heappush(minHeap, -floor)
            self.k -= 1
        
        return -sum(minHeap)
        
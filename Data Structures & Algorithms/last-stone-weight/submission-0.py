class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        self.stones = stones
        for i in range(len(self.stones)):
            self.stones[i] = self.stones[i] * (-1)
        
        heapq.heapify(self.stones)

        while len(self.stones) > 1:
            x = heapq.heappop(self.stones)
            y = heapq.heappop(self.stones)
            sub = abs(x - y)
            heapq.heappush(self.stones, -sub)
        
        if len(self.stones) == 0:
            return 0
        return -self.stones[0]
        
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.heights = heights
        rows = len(self.heights)
        cols = len(self.heights[0])
        minHeap = [[0, 0, 0]]
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))

            if (r, c) == (rows - 1, cols - 1):
                return diff
            
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newC < 0 or
                    newR >= rows or newC >= cols or
                    (newR, newC) in visit):
                    continue
                
                newDiff = max(diff, abs(self.heights[r][c] - self.heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR, newC])
        
        return 0
        
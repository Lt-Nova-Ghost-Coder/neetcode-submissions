class Solution:
    def maxArea(self, heights: List[int]) -> int:
        self.heights = heights
        maxArea = 0
        l = 0
        r = len(self.heights) - 1
        while (l < r):
            area = min(self.heights[l], self.heights[r]) * (r - l)
            maxArea = max(area, maxArea)
            if self.heights[l] <= self.heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea

        
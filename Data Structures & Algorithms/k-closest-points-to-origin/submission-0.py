class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.points = points
        self.k = k
        self.points.sort(key = lambda p : p[0] ** 2 + p[1] ** 2)
        return self.points[: self.k]
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h
        l = 1
        r = max(self.piles)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            totalTime = 0
            for i in self.piles:
                totalTime += math.ceil(float(i) / mid)
            if totalTime <= self.h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


        
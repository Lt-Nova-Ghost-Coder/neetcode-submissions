class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid
        freqMap = {}
        n = len(self.grid)

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] in freqMap:
                    freqMap[self.grid[i][j]] += 1
                else:
                    freqMap[self.grid[i][j]] = 1
        ans = [-1, -1]
        for i in range(1, (n ** 2) + 1):
            if i in freqMap:
                if freqMap[i] == 2:
                    ans[0] = i
            else:
                ans[1] = i
        return ans 
        
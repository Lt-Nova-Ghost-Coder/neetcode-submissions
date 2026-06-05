class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        rows = len(self.grid)
        cols = len(self.grid[0])

        island = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or self.grid[r][c] == "0"):
                return 
            self.grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(rows):
            for c in range(cols):
                if self.grid[r][c] == '1':
                    dfs(r, c)
                    island += 1
        return island



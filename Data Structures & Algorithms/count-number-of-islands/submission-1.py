class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        rows = len(self.grid)
        cols = len(self.grid[0]) 
        visited = set()
        island = 0
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or self.grid[r][c] == '0' or (r, c) in visited):
                return
            visited.add((r, c)) 
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            for j in range(cols):
                if self.grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    island += 1
        return island
        
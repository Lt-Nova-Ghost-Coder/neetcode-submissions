class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        
        rows = len(self.heights)
        cols = len(self.heights[0])

        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prev):
            if ((r, c) in visited or 
                r < 0 or c < 0 or
                r == rows or c == cols or
                self.heights[r][c] < prev):
                return 

            visited.add((r, c))

            dfs(r + 1, c, visited, self.heights[r][c])
            dfs(r - 1, c, visited, self.heights[r][c])
            dfs(r, c + 1, visited, self.heights[r][c])
            dfs(r, c - 1, visited, self.heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pacific, self.heights[0][c])
            dfs(rows - 1, c, atlantic, self.heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, self.heights[r][0])
            dfs(r, cols - 1, atlantic, self.heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res    

        
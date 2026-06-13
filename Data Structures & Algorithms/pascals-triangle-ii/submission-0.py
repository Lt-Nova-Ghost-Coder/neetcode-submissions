class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        self.rowIndex = rowIndex

        dp = [[1] * (i + 1) for i in range(0, self.rowIndex + 1)]
        for i in range(2, len(dp)):
            for j in range(len(dp[i])):
                if j == 0 or j == len(dp[i]) - 1:
                    continue
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp[self.rowIndex]
                   
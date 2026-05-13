class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.strs = strs
        if len(self.strs) == 1:
            return self.strs[0]
        self.strs = sorted(self.strs)
        for i in range(min(len(self.strs[0]), len(self.strs[-1]))):
            if self.strs[0][i] != self.strs[-1][i]:
                return self.strs[0][ : i]
        return self.strs[0]
        
class Solution:
    def scoreOfString(self, s: str) -> int:
        self.s = s
        Sum = 0
        for i in range(len(self.s) - 1):
            Sum += abs(ord(self.s[i]) - ord(self.s[i + 1]))
        
        return Sum

        
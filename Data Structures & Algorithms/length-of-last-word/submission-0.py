class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        self.s = s
        words = self.s.split()
        return len(words[-1])
        
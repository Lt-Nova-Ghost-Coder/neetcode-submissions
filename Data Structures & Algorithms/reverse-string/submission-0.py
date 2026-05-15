class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.s = s
        n = len(self.s)
        for i in range(n // 2):
            self.s[i], self.s[n - i - 1] = self.s[n - i - 1], self.s[i]
        return self.s

        
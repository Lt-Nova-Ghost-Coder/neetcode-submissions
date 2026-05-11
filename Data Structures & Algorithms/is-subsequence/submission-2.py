class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t
        if len(self.s) == 0:
            return True
        if len(self.s) > len(self.t):
            return False
        n = len(self.s)
        index = 0
        ch = self.s[index]
        for i in range(len(self.t)):
            if self.t[i] == ch:
                if index + 1 == n:
                    return True
                else:
                    index += 1
                    ch = self.s[index]
            else:
                continue

        return False 
        
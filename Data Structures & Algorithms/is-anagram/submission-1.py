class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t
        if len(self.s) != len(self.t):
            return False
        freq = {}
        for i in self.s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for i in self.t:
            if i in freq:
                if freq[i] == 0:
                    return False
                else:
                    freq[i] -= 1
            else:
                return False
        return True       
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t
        freq = {}
        if len(self.s) != len(self.t):
            return False
        
        for i in self.s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for i in self.t:
            if i in freq:
                if freq[i] == 0:
                    return False
                else:
                    freq[i] -= 1
            else:
                return False
        return True
        
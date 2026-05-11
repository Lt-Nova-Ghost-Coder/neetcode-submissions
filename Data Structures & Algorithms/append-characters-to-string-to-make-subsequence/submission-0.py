class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        self.s = s
        self.t = t
        if self.s == "":
            return self.t
        
        index = 0
        ch = self.t[index]
        for i in range(len(self.s)):
            if self.s[i] == ch:
                if index + 1 == len(self.t):
                    return 0
                else:
                    index += 1
                    ch = self.t[index]
            else:
                continue
                
        answer = len(self.t) - index
        return answer
        
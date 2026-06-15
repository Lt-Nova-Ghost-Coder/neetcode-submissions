class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        self.s = s
        self.t = t
        Map = {}

        for i in self.t:
            if i not in Map:
                Map[i] = 1
            else:
                Map[i] += 1
        
        for i in self.s:
            Map[i] -= 1
        for i in Map:
            if Map[i] > 0:
                return i
            else:
                continue
        return ""
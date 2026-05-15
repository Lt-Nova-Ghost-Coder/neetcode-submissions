class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        self.word1 = word1
        self.word2 = word2
        res = []
        i = 0
        while (i < len(self.word1)) and i < len(self.word2):
            res.append(self.word1[i])
            res.append(self.word2[i])
            i += 1
        
        if (i >= len(self.word1)):
            for j in range(i, len(self.word2)):
                res.append(self.word2[j])
        if (i >= len(self.word2)):
            for j in range(i, len(self.word1)):
                res.append(self.word1[j])
        
        return "".join(res)
        
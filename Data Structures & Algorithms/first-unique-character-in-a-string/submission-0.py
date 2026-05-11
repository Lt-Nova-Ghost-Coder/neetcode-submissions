class Solution:
    def firstUniqChar(self, s: str) -> int:
        self.s = s
        indexMap = {}
        for i in range(len(self.s)):
            if self.s[i] not in indexMap:
                indexMap[self.s[i]] = [i]
            else:
                indexMap[self.s[i]].append(i)
        minIndex = -1
        for i in indexMap:
            if len(indexMap[i]) == 1:
                if minIndex == -1:
                    minIndex = indexMap[i][0]
                else:
                    minIndex = min(minIndex, indexMap[i][0])
            else:
                continue
        return minIndex
        
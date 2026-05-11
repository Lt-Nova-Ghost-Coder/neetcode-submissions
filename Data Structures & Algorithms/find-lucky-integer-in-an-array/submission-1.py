class Solution:
    def findLucky(self, arr: List[int]) -> int:
        self.arr = arr
        freqMap = {}
        maxFreq = 0
        for i in self.arr:
            if i not in freqMap:
                freqMap[i] = 1
            else:
                freqMap[i] += 1
        for i in freqMap:
            if freqMap[i] == i:
                maxFreq = max(maxFreq, freqMap[i])
            else:
                continue
        if maxFreq == 0:
            return -1
        else:
            return maxFreq
        
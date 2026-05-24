class Solution:
    def maxDifference(self, s: str) -> int:
        self.s = s
        freqMap = {}
        for i in self.s:
            if i not in freqMap:
                freqMap[i] = 1
            else:
                freqMap[i] += 1
        
        maxOdd = 0
        minEven = 101

        for i in freqMap:
            if freqMap[i] % 2 == 0:
                minEven = min(minEven, freqMap[i])
            elif freqMap[i] % 2 != 0:
                maxOdd = max(maxOdd, freqMap[i])
        
        return maxOdd - minEven
        
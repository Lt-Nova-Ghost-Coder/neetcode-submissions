class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        self.arr = arr
        self.k = k
        freqMap = {}

        for i in self.arr:
            if i in freqMap:
                freqMap[i] += 1
            else:
                freqMap[i] = 1
        a = self.k

        for i in self.arr:
            if freqMap[i] > 1:
                continue
            a -= 1

            if a == 0:
                return i
        return ""
        
            
        
        
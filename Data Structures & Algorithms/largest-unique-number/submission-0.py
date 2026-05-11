class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        self.nums = nums
        freqMap = {}
        for i in self.nums:
            if i not in freqMap:
                freqMap[i] = 1
            else:
                freqMap[i] += 1
        
        maxElement = -1
        for i in freqMap:
            if freqMap[i] == 1:
                maxElement = max(maxElement, i)
            else:
                continue
        return maxElement
            
        
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        self.nums = nums
        n = len(self.nums)
        characterFreq = {}
        for i in self.nums:
            if i in characterFreq:
                characterFreq[i] += 1
            else:
                characterFreq[i] = 1
        res = []
        for i in characterFreq:
            if (characterFreq[i] > (n // 3)):
                res.append(i)
            else:
                continue
        return res
        
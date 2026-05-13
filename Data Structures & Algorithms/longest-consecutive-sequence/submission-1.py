class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        self.nums = nums
        self.nums.sort()
        sequence = set()
        length = 0
        maxLength = 0
        for i in range(len(self.nums)):
            if i == 0:
                sequence.add(self.nums[i])
                length += 1
            if (self.nums[i] - 1) in sequence:
                if self.nums[i - 1] == self.nums[i]:
                    continue
                else:
                    length += 1
                    sequence.add(self.nums[i])
            else:
                maxLength = max(maxLength, length)
                length = 1
                sequence.clear()
                sequence.add(self.nums[i])
        maxLength = max(maxLength, length)
        return maxLength
        
        
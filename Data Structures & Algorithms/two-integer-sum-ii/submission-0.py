class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        self.numbers = numbers
        self.target = target
        l = 0
        r = len(self.numbers) - 1
        while l < r:
            Sum = self.numbers[l] + self.numbers[r]
            if Sum > self.target:
                r -= 1
            elif Sum < self.target:
                l += 1 
            else:
                return [l + 1, r + 1]
        return [-1, -1]

        
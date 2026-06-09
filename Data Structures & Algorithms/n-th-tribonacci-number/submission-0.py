class Solution:
    def tribonacci(self, n: int) -> int:
        self.n = n
        first = 0
        second = 1
        third = 1
        if self.n == 0:
            return first
        if self.n == 1:
            return second
        if self.n == 2:
            return third
        
        for i in range(self.n - 2):
            num = first + second + third
            first = second
            second = third
            third = num
        
        return third
        
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.x = x
        self.n = n

        if self.x == 0:
            return 0
        if self.n == 0:
            return 1
        
        res = 1
        power = abs(self.n)

        while power:
            res = res * self.x
            power -= 1
        
        if self.n >= 0:
            return res
        else:
            return (1 / res)
class Solution:
    def isUgly(self, n: int) -> bool:
        self.n = n

        while (self.n % 2 == 0) or (self.n % 3 == 0) or (self.n % 5 == 0):
            if self.n % 2 == 0:
                self.n = self.n / 2
            elif self.n % 3 == 0:
                self.n = self.n / 3
            elif self.n % 5 == 0:
                self.n = self.n / 5

        if self.n == 1:
            return True
        return False 
        
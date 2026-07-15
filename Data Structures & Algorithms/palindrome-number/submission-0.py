class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        
        if self.x < 0:
            return False
        ans = 0
        dup = self.x
        while dup != 0:
            x = dup % 10
            ans = (ans * 10) + x
            dup = dup // 10
        
        if ans == self.x:
            return True
        return False
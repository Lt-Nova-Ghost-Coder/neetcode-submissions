class Solution:
    def isPalindrome(self, s: str) -> bool:
        self.s = s
        l = 0
        r = len(self.s) - 1
        while l <= r:
            if self.s[l].lower() == self.s[r].lower():
                l += 1
                r -= 1
            elif (not (self.s[l].isalnum())):
                l += 1
            elif (not (self.s[r].isalnum())):
                r -= 1
            else:
                return False
        return True

        
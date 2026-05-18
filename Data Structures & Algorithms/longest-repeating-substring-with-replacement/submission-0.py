class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        self.s = s
        self.k = k
        charSet = set(self.s)
        res = 0
        for c in charSet:
            count = l = 0
            for r in range(len(self.s)):
                if self.s[r] == c:
                    count += 1
                
                while (r - l + 1) - count > self.k:
                    if self.s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res

        
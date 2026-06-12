class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        self.senate = senate
        D = deque()
        R = deque()

        for i in range(len(self.senate)):
            if self.senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)
        while D and R:
            d = D.popleft()
            r = R.popleft()

            if r < d:
                R.append(r + len(self.senate))
            else:
                D.append(d + len(self.senate))
        
        if not R and D:
            return "Dire"
        else:
            return "Radiant"
        
        
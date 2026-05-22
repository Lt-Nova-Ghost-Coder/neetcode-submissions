class Solution:
    def countSeniors(self, details: List[str]) -> int:
        self.details = details
        count = 0
        for i in range(len(self.details)):
            age = int(self.details[i][-4] + self.details[i][-3])
            if age > 60:
                count += 1
            else:
                continue
        return count
        
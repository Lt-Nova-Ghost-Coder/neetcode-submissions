class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        self.bills = bills
        five = 0
        ten = 0
        twenty = 0

        for i in range(len(self.bills)):
            if self.bills[i] == 5:
                five += 1
            elif self.bills[i] == 10:
                if five == 0:
                    return False
                else:
                    ten += 1
                    five -= 1
            elif self.bills[i] == 20:
                if ten >= 1 and five >= 1:
                    twenty += 1
                    ten -= 1
                    five -= 1
                elif ten == 0 and five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False
            else:
                continue
        return True

        
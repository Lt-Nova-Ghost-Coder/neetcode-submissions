class Solution:
    def calPoints(self, operations: List[str]) -> int:
        self.operations = operations
        stack = []
        Sum = 0
        for i in self.operations:
            if i == '+':
                stack.append(stack[-1] + stack[-2])
                Sum += stack[-1]
            elif i == 'C':
                Sum -= stack.pop()
            elif i == 'D':
                stack.append(stack[-1] * 2)
                Sum += stack[-1]
            else:
                stack.append(int(i))
                Sum += stack[-1]
        
        return Sum


        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.tokens = tokens
        stack = []
        for i in range(len(self.tokens)):
            if self.tokens[i] == '+':
                opr = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(opr)
            elif self.tokens[i] == '-':
                opr = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(opr)
            elif self.tokens[i] == '*':
                opr = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(opr)
            elif self.tokens[i] == '/':
                opr = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(opr)
            else:
                stack.append(int(self.tokens[i]))
        
        return int(stack[-1])
        
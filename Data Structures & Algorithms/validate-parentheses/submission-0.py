class Solution:
    def isValid(self, s: str) -> bool:
        self.s = s
        stack = []
        for i in range(len(self.s)):
            if self.s[i] in ('(', '[', '{'):
                stack.append(self.s[i])
            else:
                if self.s[i] == ')':
                    if stack:
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
                elif self.s[i] == ']':
                    if stack:
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
                elif self.s[i] == '}':
                    if stack:
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
                else:
                    continue
        if len(stack) == 0:
            return True
        else:
            return False
        
class MinStack:

    def __init__(self):
        self.mainStack = []
        self.mainTop = None
        self.minStack = []
        self.minTop = None
        

    def push(self, val: int) -> None:
        self.val = val
        self.mainStack.append(self.val)
        self.mainTop = self.mainStack[-1]

        if not self.minStack:
            self.minStack.append(self.val)
            self.minTop = self.minStack[-1]
        else:
            if self.minStack[-1] >= self.val:
                self.minStack.append(self.val)
                self.minTop = self.minStack[-1]
        

    def pop(self) -> None:
        if not self.mainStack:
            return None
        
        val = self.mainStack.pop()
        if not self.mainStack:
            self.mainTop = None
        else:
            self.mainTop = self.mainStack[-1]
        
        if self.minTop == val:
            self.minStack.pop()
            if not self.minStack:
                self.minTop = None
            else:
                self.minTop = self.minStack[-1]
        

    def top(self) -> int:
        return self.mainTop
        

    def getMin(self) -> int:
        return self.minTop
        

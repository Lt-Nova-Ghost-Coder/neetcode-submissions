class MyStack:

    def __init__(self):
        from collections import deque
        self.q = deque([])
        

    def push(self, x: int) -> None:
        self.x = x
        self.q.appendleft(self.x)

    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        if not self.q:
            return None
        return self.q[0]
        

    def empty(self) -> bool:
        if not self.q:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class MinStack:

    def __init__(self):
        self.stack = []
        self.mval = float('inf')

    def push(self, val: int) -> None:
        if val < self.mval:
            self.mval = val
        self.stack.append(val)            
            

    def pop(self) -> None:
        val = self.stack.pop()
        if self.stack:
            self.mval = min(self.stack)
        else:
            self.mval = float('inf')
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mval

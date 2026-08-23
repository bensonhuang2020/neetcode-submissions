class MinStack:

    def __init__(self):
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if self.min_stack:
            self.min_stack.append((val, min(self.min_stack[-1][1], val)))
        else:
            self.min_stack.append((val, val))
        

    def pop(self) -> None:
        return self.min_stack.pop(-1)[0]
        

    def top(self) -> int:
        return self.min_stack[-1][0]
        

    def getMin(self) -> int:
        return self.min_stack[-1][1]

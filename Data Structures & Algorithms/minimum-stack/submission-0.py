class MinStack:
    def __init__(self):
        self.stack = []      # holds actual values
        self.min_stack = []  # holds min so far at each level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # push new min (either val, or previous min if val is bigger)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
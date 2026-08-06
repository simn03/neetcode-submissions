class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = math.inf

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            self.stack.append(val - self.min_val)
            self.min_val = min(self.min_val, val)
        
        # print(f"push ({self.min_val})", self.stack)


    def pop(self) -> None:
        last = self.stack.pop()

        if last < 0:
            self.min_val = -last + self.min_val

        # print(f"pop ({self.min_val},)", self.stack)

    def top(self) -> int:
        last = self.stack[-1]

        if last < 0:
            return int(self.min_val)

        return last + self.min_val


    def getMin(self) -> int:
        return int(self.min_val)
        

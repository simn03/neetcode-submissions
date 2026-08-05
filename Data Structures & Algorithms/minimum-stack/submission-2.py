class MinStack:

    def __init__(self):
        self.stack = []
        # is exactly as long and tracks min element so far
        # except for being seeded with "MAX_INT" to avoid errors later
        self.min_stack = [1 << 31] 


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]
        

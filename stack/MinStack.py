class MinStack:

    def __init__(self):
        self.stack = None
        

    def push(self, val: int) -> None:
        if self.stack == None:
            self.stack = [val]
            self.top_i = 0

            self.mins = [val]
            self.min_i = 0
        else:
            self.stack.append(val)
            self.top_i += 1

            if val <= self.mins[self.min_i]:
                self.mins.append(val)
                self.min_i += 1
        

    def pop(self) -> None:
        if self.top_i == 0:
            self.stack = None
            self.top_i = None
            
            self.mins = None
            self.min_i = None
        else:
            if self.stack[self.top_i] == self.mins[self.min_i]:
                self.mins = self.mins[:self.min_i]
                self.min_i -= 1

            self.stack = self.stack[:self.top_i]
            self.top_i -= 1

        

    def top(self) -> int:
        return self.stack[self.top_i]
        

    def getMin(self) -> int:
        return self.mins[self.min_i]

minStack = MinStack()

funcs = [
    "push",
    "push",
    "push",
    "top",
    "pop",
    "getMin",
    "pop",
    "getMin",
    "pop",
    "push",
    "top",
    "getMin",
    "push",
    "top",
    "getMin",
    "pop",
    "getMin",
]
vals = [
    [2147483646],
    [2147483646],
    [2147483647],
    [],
    [],
    [],
    [],
    [],
    [],
    [2147483647],
    [],
    [],
    [-2147483648],
    [],
    [],
    [],
    [],
]

for func, val in zip(funcs, vals):
    if len(val) == 1:
        getattr(minStack, func)(val[0])
    else:
        getattr(minStack, func)()

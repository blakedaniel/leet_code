class MinStack:

    def __init__(self):
        self.values = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.values) == ()
        self.values.append(val)
        if val < self.min[0]:
            self.min.insert(0, val)
        else:
            pass

    def pop(self) -> None:
        val = self.values.pop()
        if val == self.min:
            pass
        # if pop is the minumum need to redefine minumum

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min[0]

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(val)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getMin()
obj.pop()
obj.top()
obj.getMin()

class Test():
    def __init__(self, lst:list):
        self.lst = lst
        self.first = lst[0]
        self.tail = lst[1:]
        if len(lst) == 1:
            self.tail = None
        
    def __repr__(self) -> str:
        return str(self.lst)
    
test1 = Test([1, 2, 3])
test2 = test1

print('TEST1:', test1)
print('TEST2:', test2)



print('TEST1:', test1)
print('TEST2:', test2)

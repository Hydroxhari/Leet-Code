class MinStack(object):

    def __init__(self):
        self.s=[]
        return 

    def push(self, val):
        self.s.append(val)
        return

    def pop(self):
        self.s.pop()
        return

    def top(self):
        return self.s[-1]
        

    def getMin(self):
        return min(self.s)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
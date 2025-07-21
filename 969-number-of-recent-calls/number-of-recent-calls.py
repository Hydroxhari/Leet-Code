class RecentCounter(object):

    def __init__(self):
        self.l=[]

    def ping(self, t):
        r=t-3000
        while self.l and self.l[0]<r:
            self.l.pop(0)
        self.l.append(t)
        return len(self.l)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
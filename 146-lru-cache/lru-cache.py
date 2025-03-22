class LRUCache(object):

    def __init__(self, c):
        self.d=OrderedDict()
        self.c=c

    def get(self, k):
        if k not in self.d:
            return -1
        
        v=self.d.pop(k)
        self.d[k]=v
        return self.d[k]
        

    def put(self, k, v):
        if k in self.d:
            self.d.pop(k)
        self.d[k]=v

        if len(self.d)>self.c:
            self.d.popitem(last=False)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
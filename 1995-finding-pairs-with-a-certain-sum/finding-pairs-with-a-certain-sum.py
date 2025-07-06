class FindSumPairs(object):

    def __init__(self, n1, n2):
        self.c1=Counter(n1)
        self.c2=Counter(n2)
        self.n1=n1
        self.n2=n2

    def add(self, i, v):
        ov=self.n2[i]
        nv=self.n2[i]+v
        self.n2[i]=nv
        self.c2[ov]-=1
        self.c2[nv]+=1

    def count(self, t):
        c=0
        for i,j in self.c1.items():
            if t-i in self.c2:
                c+=j*self.c2[t-i]
        return c



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
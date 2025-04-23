class Solution(object):
    def countLargestGroup(self, n):
        h=defaultdict(int)
        m=0
        for i in range(1,n+1):
            e=0
            for j in str(i):
                e+=int(j)
            h[e]+=1
            m=max(m,h[e])
        return h.values().count(m)

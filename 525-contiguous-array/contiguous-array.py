class Solution(object):
    def findMaxLength(self, n):

        d=defaultdict(int)
        d[0]=-1
        s=0
        m=0
        for i in range(len(n)):
            if n[i]==0:
                s+=-1
            else:
                s+=1
            if s in d:
                m=max(m,i-d[s])
            else:
                d[s]=i
        return m
            

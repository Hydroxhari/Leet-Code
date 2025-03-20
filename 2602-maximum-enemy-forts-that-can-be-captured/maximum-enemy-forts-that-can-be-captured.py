class Solution(object):
    def captureForts(self, f):
        
        m=0
        s=len(f)
        for i in range(len(f)):
            if f[i]==1:
                s=i
            elif f[i]==-1:
                m=max(m,i-s-1)
                s=len(f)
        s=0
        for i in range(len(f)-1,-1,-1):
            if f[i]==1:
                s=i
            elif f[i]==-1:
                m=max(m,s-i-1)
                s=0
        
        return m

        
class Solution(object):
    def findMaxLength(self, n):
        for i in range(len(n)):
            if n[i]==0:
                n[i]=-1
        
        d={}

        s=0
        m=0

        for i in range(len(n)):
            s+=n[i]

            if 0+s in d:
                m=max(m,i-d[0+s])
            else:
                d[s]=i
            
            if s==0:
                m=max(m,i+1)
        return m
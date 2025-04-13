class Solution(object):
    def maximumTripletValue(self, n):
        
        e=float('-inf')
        d=0
        m=0

        for i in range(len(n)):
            e=max(e,n[i])
            if i>=2:
                m=max(m,d*n[i])
            if i>=1:
                d=max(d,e-n[i])
        
        return m
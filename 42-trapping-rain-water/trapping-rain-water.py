class Solution(object):
    def trap(self, h):

        l=[]
        m=0
        for i in h:
            m=max(m,i)
            l.append(m)
        
        r=[]
        m=0
        for i in h[::-1]:
            m=max(m,i)
            r.append(m)
        r=r[::-1]
        
        c=0
        for i in range(len(h)):
            c+=min(l[i],r[i])-h[i]
        return c





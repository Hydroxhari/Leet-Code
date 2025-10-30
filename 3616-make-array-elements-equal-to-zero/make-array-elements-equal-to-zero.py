class Solution(object):
    def countValidSelections(self, n):

        def tr(i,d):
            t=n[:]
            while 0<=i<len(n):
                if t[i]!=0:
                    t[i]-=1
                    d=-d
                i+=d
            return set(t)=={0}

        c=0
        for i in range(len(n)):
            if n[i]==0:
                c+=tr(i,1)
                c+=tr(i,-1)
        
        return c

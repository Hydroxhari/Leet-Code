class Solution(object):
    def permute(self, n):

        r=[]
        u=[False]*len(n)

        def bt(l):
            if len(l)==len(n):
                r.append(l[:])
                return
            
            for i in range(len(n)):
                if not u[i]:
                    u[i]=True
                    l.append(n[i])
                    bt(l)
                    l.pop()
                    u[i]=False
        bt([])
        return r
        
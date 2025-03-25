class Solution(object):
    def permute(self, n):

        r=[]
        s=set(n)

        def bt(l):
            if len(l)==len(n):
                r.append(l[:])
                return
            
            for i in s:
                if i not in l:
                    l.append(i)
                    bt(l)
                    l.pop()
        bt([])
        return r
        
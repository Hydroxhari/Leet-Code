class Solution(object):
    def combine(self, n, k):

        l=list(range(1,n+1))

        r=[]
        def bt(s,ls):
            if len(ls)==k:
                r.append(ls)
                return
            
            for i in range(s,n):
                bt(i+1,ls+[l[i]])

        bt(0,[])
        return r
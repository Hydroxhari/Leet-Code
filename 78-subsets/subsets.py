class Solution(object):
    def subsets(self, n):

        r=[]

        def bt(s,l):
            r.append(l[:])
            for i in range(s,len(n)):
                l.append(n[i])
                bt(i+1,l)
                l.pop()
        
        bt(0,[])
        return r

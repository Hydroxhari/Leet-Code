class Solution(object):
    def subsets(self, n):

        r=[]

        def bt(s,l):
            r.append(l[:])
            for i in range(s,len(n)):
                bt(i+1,l+[n[i]])
        
        bt(0,[])
        return r

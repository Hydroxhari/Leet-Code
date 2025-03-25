class Solution(object):
    def subsetsWithDup(self, n):
        r=[]
        n.sort()

        def bt(s,l):
            r.append(l[:])
            for i in range(s,len(n)):
                if i>s and n[i]==n[i-1]:
                    continue
                l.append(n[i])
                bt(i+1,l)
                l.pop()
            
        
        bt(0,[])
        return r
        
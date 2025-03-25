class Solution(object):
    def combinationSum2(self, c, t):
        c.sort()
        r=[]

        def bt(s,l,t):
            if t==0:
                r.append(l[:])
                return 
            
            for i in range(s,len(c)):
                if i>s and c[i]==c[i-1]:
                    continue
                if t<c[i]:
                    break
                l.append(c[i])
                bt(i+1,l,t-c[i])
                l.pop()
            
        bt(0,[],t)
        return r
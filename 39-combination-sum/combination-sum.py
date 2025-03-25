class Solution(object):
    def combinationSum(self, c, k):
        s=[]
        c.sort()

        def bt(st,l,t):
            if t==0:
                s.append(l[:])
                return
            
            for i in range(st,len(c)):
                if t<c[i]:
                    break
                l.append(c[i])
                bt(i,l,t-c[i])
                l.pop()

        bt(0,[],k)
        return s


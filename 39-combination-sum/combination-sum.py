class Solution(object):
    def combinationSum(self, c, k):
        s=set()
        c.sort()

        def bt(l,t):
            if t==0:
                s.add(tuple(sorted(l[:])))
                return
            
            for i in range(len(c)):
                if t-c[i]>=0:
                    l.append(c[i])
                    bt(l,t-c[i])
                    l.pop()
                else:
                    return
        bt([],k)
        return list(list(i) for i in s)


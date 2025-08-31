class Solution(object):
    def combinationSum(self, l, t):

        s=set()

        def bt(t,al):
            if t==0:
                nt=tuple(sorted(al))
                s.add(nt)
            
            for i in l:
                if t-i>=0:
                    bt(t-i,al+[i])
        
        bt(t,[])

        return list(s)
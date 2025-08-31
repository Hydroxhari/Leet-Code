class Solution(object):
    def combinationSum(self, l, t):

        s=set()

        def bt(i,t,al):
            if t==0:
                nt=tuple(sorted(al))
                s.add(nt)
            if i>=len(l) or t<0:
                return 0
            take = bt(i,t-l[i],al+[l[i]])
            dtake= bt(i+1,t,al)

        bt(0,t,[])

        return list(s)
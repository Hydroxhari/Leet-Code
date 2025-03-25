class Solution(object):
    def maxPathSum(self, r):
        self.m=float('-inf')
        def bt(r):
            if not r:
                return 0
            
            lm=max(bt(r.left),0)
            rm=max(bt(r.right),0)

            self.m=max(self.m,lm+rm+r.val)


            return r.val+max(lm,rm)

        bt(r)
        return self.m

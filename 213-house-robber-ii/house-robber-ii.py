class Solution(object):
    def rob(self, n):

        if len(n)==1:
            return n[0]
        if len(n)==2:
            return max(n)

        me=defaultdict(int)
        def dp(i,j):
            if (i,j) in me:
                return me[(i,j)]
            if i>=len(n)-j:
                return 0
            
            t=n[i]+dp(i+2,j)
            dt=dp(i+1,j)

            me[(i,j)] = max(t,dt)
            return me[(i,j)]
        
        return max(dp(0,1),dp(1,0))
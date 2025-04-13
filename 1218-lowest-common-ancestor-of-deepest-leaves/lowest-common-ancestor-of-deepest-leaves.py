class Solution(object):
    def lcaDeepestLeaves(self, r):

        def ht(r):
            if not r:
                return 0
            return 1+max(ht(r.left),ht(r.right))
        
        h=ht(r)
    
        def dfs(n,d):
            if not n:
                return None
            if d==h:
                return n
            
            l = dfs(n.left,d+1)
            r = dfs(n.right,d+1)

            if l and r:
                return n
            return l or r
            
        return dfs(r,1)
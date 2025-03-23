class Solution(object):
    def isBalanced(self, r):
        def dfs(r):
            if not r:
                return 0
            
            ln=dfs(r.left)
            rn=dfs(r.right)

            if ln==-1 or rn==-1 or abs(ln-rn)>1:
                return -1
            
            return 1+max(ln,rn)
        
        return dfs(r)!=-1
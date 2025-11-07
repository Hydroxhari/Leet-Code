class Solution(object):
    def pathSum(self, r, t):

        a=[]
        def dfs(n,c,l):
            if not n:
                return
            
            c+=n.val
            l.append(n.val)

            if c==t and n.left==None and n.right==None:
                a.append(l[:])
            
            dfs(n.left,c,l[:])
            dfs(n.right,c,l[:])

        dfs(r,0,[])
        return a
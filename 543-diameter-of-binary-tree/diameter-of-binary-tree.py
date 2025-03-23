class Solution(object):
    def diameterOfBinaryTree(self, r):

        self.d=0

        def dfs(r):
            if not r:
                return 0

            ln=dfs(r.left)
            rn=dfs(r.right)

            self.d=max(self.d,ln+rn) 

            return 1+max(ln,rn)
        dfs(r)
        return self.d
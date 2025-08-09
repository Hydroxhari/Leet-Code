class Solution(object):
    def searchBST(self, r, v):
        def t(r):
            if not r:
                return None
            elif r.val==v:
                return r
            elif v<r.val:
                return t(r.left)
            elif v>r.val:
                return t(r.right)
            else:
                return None
        
        return t(r)
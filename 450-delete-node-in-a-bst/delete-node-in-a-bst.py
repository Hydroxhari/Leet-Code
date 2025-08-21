class Solution(object):
    def deleteNode(self, r, k):
        if not r:
            return r
        elif k>r.val:
            r.right = self.deleteNode(r.right,k)
        elif k<r.val:
            r.left = self.deleteNode(r.left,k)
        else:
            if not r.left and not r.right:
                return None
            elif  not r.right:
                return r.left
            elif not r.left:
                return r.right
            else:
                c=r.right
                while c.left:
                    c=c.left
                r.val=c.val
                r.right = self.deleteNode(r.right,c.val)
        return r
class Solution(object):
    def isValidBST(self, r):
        
        def bst(v,lf,ri):
            if not v:
                return True
            if not (lf<v.val<ri):
                return False
            
            return bst(v.left,lf,v.val) and bst(v.right,v.val,ri)

        return bst(r,float('-inf'),float('inf'))
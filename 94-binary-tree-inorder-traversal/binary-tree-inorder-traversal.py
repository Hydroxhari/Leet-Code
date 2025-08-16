class Solution(object):
    def inorderTraversal(self, r):

        l=[]
        def it(n):
            if not n:
                return    
            it(n.left)
            l.append(n.val)
            it(n.right)
            
        it(r)
        return l
        
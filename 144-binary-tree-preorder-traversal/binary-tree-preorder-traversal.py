class Solution(object):
    def preorderTraversal(self, r):

        l=[]

        def it(n):
            if not n:
                return
            
            l.append(n.val)
            it(n.left)
            it(n.right)
        it(r)
        return l
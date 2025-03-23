class Solution(object):
    def invertTree(self, r):
        if not r:
            return None

        t=TreeNode(r.val)
        t.left=self.invertTree(r.right)
        t.right=self.invertTree(r.left)

        return t
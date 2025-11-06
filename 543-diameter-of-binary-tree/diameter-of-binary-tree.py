class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.ans

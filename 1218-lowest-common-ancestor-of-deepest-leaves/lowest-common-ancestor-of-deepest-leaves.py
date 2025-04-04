class Solution:
    def ht(self, node):
        if not node:
            return 0
        return max(self.ht(node.left), self.ht(node.right)) + 1
    
    def dfs(self, node):
        if not node:
            return None
        left, right = self.ht(node.left), self.ht(node.right)
        if left == right:
            return node
        if left > right:
            return self.dfs(node.left)
        if left < right:
            return self.dfs(node.right)

    def lcaDeepestLeaves(self, root):
        return self.dfs(root)
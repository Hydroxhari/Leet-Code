class Solution(object):
    def goodNodes(self, root):
        if not root:
            return 0

        def dfs(node, currmax):
            if not node:
                return
            if node.val >= currmax:
                count[0] += 1
                currmax = node.val
            dfs(node.left, currmax)
            dfs(node.right, currmax)
        count = [0]
        dfs(root, root.val)
        return count[0]

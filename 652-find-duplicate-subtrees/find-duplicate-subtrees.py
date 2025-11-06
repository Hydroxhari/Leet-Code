from collections import defaultdict

class Solution(object):
    def findDuplicateSubtrees(self, r):
        d = defaultdict(int)
        res = []

        def dfs(node):
            if not node:
                return "#"
            
            left = dfs(node.left)
            right = dfs(node.right)

            # use plain string concatenation instead of f-string
            serial = str(node.val) + "," + left + "," + right
            d[serial] += 1

            if d[serial] == 2:
                res.append(node)
            
            return serial
        
        dfs(r)
        return res

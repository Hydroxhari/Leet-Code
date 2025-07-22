from collections import defaultdict

class Solution(object):
    def pathSum(self, root, target):
        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            count = prefix[curr_sum - target]

            prefix[curr_sum] += 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix[curr_sum] -= 1  # backtrack

            return count

        prefix = defaultdict(int)
        prefix[0] = 1
        return dfs(root, 0)

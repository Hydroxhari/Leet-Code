class Solution(object):
    def pathSum(self, root, target):
        if not root:
            return 0

        def count_paths_from_node(node, curr_sum):
            if not node:
                return 0
            count = 0
            if node.val == curr_sum:
                count += 1
            count += count_paths_from_node(node.left, curr_sum - node.val)
            count += count_paths_from_node(node.right, curr_sum - node.val)
            return count

        return (count_paths_from_node(root, target) +
                self.pathSum(root.left, target) +
                self.pathSum(root.right, target))

from collections import deque

class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        
        # Use deque for BFS (node, min_value, max_value)
        q = deque([(root, float('-inf'), float('inf'))])
        
        while q:
            node, low, high = q.popleft()
            
            if not node:
                continue
            
            # Check if the current node violates the BST property
            if not (low < node.val < high):
                return False
            
            # Left child: max value should be the current node's value
            if node.left:
                q.append((node.left, low, node.val))
            
            # Right child: min value should be the current node's value
            if node.right:
                q.append((node.right, node.val, high))
        
        return True

class Solution(object):
    def sortedArrayToBST(self, n): 

        if not n:
            return None
        
        def dfs(nums):
            if not nums:
                return None
            m = len(nums) // 2
            root = TreeNode(nums[m])
            root.left = dfs(nums[:m])
            root.right = dfs(nums[m+1:])
            return root
        
        return dfs(n)

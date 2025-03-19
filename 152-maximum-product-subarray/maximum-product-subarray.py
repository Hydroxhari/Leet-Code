class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        # Initialize variables
        max_prod = nums[0]  # Maximum product so far
        min_prod = nums[0]  # Minimum product so far (to handle negative numbers)
        result = nums[0]    # Final result
        
        for i in range(1, len(nums)):
            # If the current number is negative, swap max_prod and min_prod
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod
            
            # Update max_prod and min_prod
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])
            
            # Update the result
            result = max(result, max_prod)
        
        return result
class Solution:
    def longestNiceSubarray(self, nums):
        left = 0
        mask = 0  # Stores OR of all elements in the window
        max_length = 0

        for right in range(len(nums)):
            while (mask & nums[right]) != 0:  # If conflict, remove elements from left
                mask ^= nums[left]
                left += 1
            
            mask |= nums[right]  # Add current number to the OR mask
            max_length = max(max_length, right - left + 1)

        return max_length

class Solution(object):
    def minimumIndex(self, nums):
                # Step 1: Find the dominant element (Boyer-Moore Voting Algorithm)
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Step 2: Validate if the candidate is actually dominant
        total_count = nums.count(candidate)
        if total_count <= len(nums) // 2:
            return -1  # No dominant element

        # Step 3: Traverse to find the minimum valid split
        left_count = 0
        for i in range(len(nums) - 1):
            if nums[i] == candidate:
                left_count += 1
            
            left_size = i + 1
            right_size = len(nums) - left_size

            # Check dominance condition in both subarrays
            if left_count * 2 > left_size and (total_count - left_count) * 2 > right_size:
                return i
        
        return -1
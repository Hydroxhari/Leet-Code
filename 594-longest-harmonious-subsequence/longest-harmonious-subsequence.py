from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        # Create a frequency dictionary
        freq = Counter(nums)
        max_length = 0
        
        # Iterate through the dictionary
        for key in freq:
            if key + 1 in freq:  # Check for harmonious pair
                # Calculate total count of the pair
                max_length = max(max_length, freq[key] + freq[key + 1])
        
        return max_length

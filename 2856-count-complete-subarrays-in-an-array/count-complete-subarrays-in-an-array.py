from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums):
        total_unique = len(set(nums))
        n = len(nums)
        count = 0
        freq = defaultdict(int)
        
        left = 0
        
        for right in range(n):
            freq[nums[right]] += 1

            while len(freq) == total_unique:
                count += n - right  # all subarrays from left to end are complete
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        
        return count

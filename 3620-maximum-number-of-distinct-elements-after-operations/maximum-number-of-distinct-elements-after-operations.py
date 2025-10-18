class Solution:
    def maxDistinctElements(self, nums, k):
        nums.sort()
        placed = -10**18  # last used number
        count = 0
        
        for x in nums:
            # The smallest we can place for current element
            start = max(x - k, placed + 1)
            if start <= x + k:
                placed = start
                count += 1
                
        return count

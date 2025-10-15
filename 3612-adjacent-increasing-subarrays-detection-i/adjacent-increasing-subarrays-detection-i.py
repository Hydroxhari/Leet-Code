class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)
        inc = [1] * n  # inc[i] = length of increasing subarray ending at i

        # Step 1: build increasing lengths
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        # Step 2: check two adjacent increasing subarrays of size k
        for i in range(k - 1, n - k):
            if inc[i] >= k and inc[i + k] >= k:
                return True

        return False

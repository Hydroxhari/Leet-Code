class Solution:
    def numSubseq(self, nums, target):
        MOD = 10**9 + 7
        nums.sort()

        # Precompute 2^i up to length of nums
        pow2 = [1] * len(nums)
        for i in range(1, len(nums)):
            pow2[i] = (pow2[i-1] * 2) % MOD

        left, right = 0, len(nums) - 1
        count = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                # All combinations of elements between left and right are valid
                count = (count + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return count

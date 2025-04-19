import bisect

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            left = bisect.bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect.bisect_right(nums, upper - nums[i], i + 1, n)
            count += (right - left)

        return count

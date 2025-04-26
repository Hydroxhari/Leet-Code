from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_min = -1  # the last index where nums[i] == minK
        last_max = -1  # the last index where nums[i] == maxK
        last_invalid = -1  # the last index where nums[i] < minK or nums[i] > maxK
        res = 0  # the final result (number of valid subarrays)

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid = i  # If num is invalid, reset window
            if num == minK:
                last_min = i  # update the last place we found minK
            if num == maxK:
                last_max = i  # update the last place we found maxK

            # Now, if both minK and maxK have appeared **after** last_invalid,
            # We can form (min(last_min, last_max) - last_invalid) subarrays ending at i
            res += max(0, min(last_min, last_max) - last_invalid)

        return res

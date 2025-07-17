class Solution(object):
    def moveZeroes(self, nums):
        pos = 0  # Position to place next non-zero
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

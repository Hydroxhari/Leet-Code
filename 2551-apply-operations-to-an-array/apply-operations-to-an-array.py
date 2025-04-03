class Solution(object):
    def applyOperations(self, nums):
        k = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[k]:
                nums[k], nums[i] = nums[k]*2, 0
            k += 1
        n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n], nums[i] = nums[i], nums[n]
                n += 1
        return nums
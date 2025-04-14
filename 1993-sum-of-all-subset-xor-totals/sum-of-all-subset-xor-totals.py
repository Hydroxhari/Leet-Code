class Solution:
    def subsetXORSum(self, nums):
        total = 0
        for num in nums:
            total |= num  # bitwise OR of all elements
        return total * (1 << (len(nums) - 1))  # total * 2^(n - 1)
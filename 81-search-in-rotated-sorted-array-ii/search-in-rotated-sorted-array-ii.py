class Solution(object):
    def search(self, nums, target):
        s=set(nums)
        return target in s
        
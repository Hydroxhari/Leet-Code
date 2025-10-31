class Solution(object):
    def getSneakyNumbers(self, nums):
        return [x for x, n in Counter(nums).items() if n == 2]
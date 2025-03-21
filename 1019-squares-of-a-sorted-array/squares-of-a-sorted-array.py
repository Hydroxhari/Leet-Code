class Solution(object):
    def sortedSquares(self, nums):
        res = [n**2 for n in nums]

        return sorted(res)
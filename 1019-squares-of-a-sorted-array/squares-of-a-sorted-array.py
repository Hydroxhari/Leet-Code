class Solution(object):
    def sortedSquares(self, n):
        m=[i**2 for i in n]
        m.sort()
        return m
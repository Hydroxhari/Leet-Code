class Solution(object):
    def findDifference(self, n, m):
        return [list(set(n)-(set(n)&set(m))) , list(set(m)-(set(n)&set(m)))]
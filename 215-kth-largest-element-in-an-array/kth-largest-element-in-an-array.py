class Solution(object):
    def findKthLargest(self, n, k):
        return sorted(n)[-k]
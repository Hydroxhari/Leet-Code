class Solution(object):
    def findKthLargest(self, n, k):
        return heapq.nlargest(k,n)[-1]
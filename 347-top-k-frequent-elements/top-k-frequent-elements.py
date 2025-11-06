import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, n, k):
        c = Counter(n)
        return heapq.nlargest(k, c.keys(), key=lambda x: c[x])

import heapq

class Solution(object):
    def maxSubsequence(self, n, k):
        # Pair each value with its index
        paired = [(val, i) for i, val in enumerate(n)]

        # Pick k largest values using value as key
        top_k = heapq.nlargest(k, paired, key=lambda x: x[0])

        # Sort by original index to preserve subsequence order
        top_k.sort(key=lambda x: x[1])

        # Extract just the values
        return [val for val, idx in top_k]

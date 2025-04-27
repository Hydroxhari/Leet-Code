import heapq

class Solution(object):
    def kClosest(self, points, k):
        return heapq.nsmallest(k, points, key=lambda point: point[0]**2 + point[1]**2)

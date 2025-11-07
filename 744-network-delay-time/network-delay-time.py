from collections import defaultdict
import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))

        heap = [(0, k)]  # (time, node)
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            for nei, wt in g[node]:
                heapq.heappush(heap, (time + wt, nei))

        return max(dist.values()) if len(dist) == n else -1

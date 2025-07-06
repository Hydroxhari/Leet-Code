from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the graph
        dalmurecio = defaultdict(list)
        for u, v, start, end in edges:
            dalmurecio[u].append((v, start, end))

        # Step 2: Priority queue: (current_time, current_node)
        heap = [(0, 0)]
        visited = dict()  # (node) -> earliest_time_seen

        while heap:
            time, node = heapq.heappop(heap)

            if node == n - 1:
                return time

            # Skip if we've already seen a better time
            if node in visited and visited[node] <= time:
                continue
            visited[node] = time

            # Try all outgoing edges
            for nei, start, end in dalmurecio[node]:
                # If current time is within valid edge window
                if start <= time <= end:
                    heapq.heappush(heap, (time + 1, nei))
                # If we must wait until the edge becomes available
                elif time < start:
                    heapq.heappush(heap, (start + 1, nei))

            # You can also choose to wait at current node
            heapq.heappush(heap, (time + 1, node))

        return -1
from collections import defaultdict
import heapq

class Solution(object):
    def countPaths(self, n, r):
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v, t in r:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        # Step 2: Dijkstra's Initialization
        mod = 10**9 + 7
        min_time = [float('inf')] * n   # Stores the shortest time to reach each node
        path_count = [0] * n            # Stores the number of ways to reach each node
        min_time[0] = 0                 # Start from node 0 with time 0
        path_count[0] = 1               # There's one way to start from node 0

        # Priority queue to store (time, node)
        pq = [(0, 0)]  # (time to reach the node, node)

        # Step 3: Dijkstra's Algorithm
        while pq:
            current_time, node = heapq.heappop(pq)

            # If the current time is greater than the recorded shortest time, skip it
            if current_time > min_time[node]:
                continue
            
            # Explore all neighbors
            for neighbor, travel_time in graph[node]:
                new_time = current_time + travel_time

                # Found a **shorter path** to the neighbor
                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    path_count[neighbor] = path_count[node]
                    heapq.heappush(pq, (new_time, neighbor))

                # Found **another path** with the **same shortest time**
                elif new_time == min_time[neighbor]:
                    path_count[neighbor] = (path_count[neighbor] + path_count[node]) % mod

        # Step 4: Return the number of shortest paths to node n-1
        return path_count[n - 1]

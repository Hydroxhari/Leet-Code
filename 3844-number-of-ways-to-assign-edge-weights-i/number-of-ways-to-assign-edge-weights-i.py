from collections import defaultdict, deque

MOD = 10**9 + 7

class Solution(object):
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7
        n=len(edges)+1
        # Step 1: Build tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Find depth of deepest node using BFS
        depth = [0] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([(1, 0)])  # (node, depth)

        max_depth = 0

        while queue:
            node, d = queue.popleft()
            visited[node] = True
            depth[node] = d
            max_depth = max(max_depth, d)
            for nei in graph[node]:
                if not visited[nei]:
                    queue.append((nei, d + 1))

        # Step 3: Compute number of ways
        if max_depth == 0:
            return 0  # no path to any deeper node

        return pow(2, max_depth - 1, MOD)
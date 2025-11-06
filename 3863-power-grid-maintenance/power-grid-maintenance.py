from collections import defaultdict
import heapq

class Solution:
    def processQueries(self, c, connections, queries):
        parent = list(range(c + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Build Union-Find
        for u, v in connections:
            union(u, v)

        # Step 2: Build component heaps
        component_heaps = defaultdict(list)
        online = [True] * (c + 1)
        for i in range(1, c + 1):
            root = find(i)
            heapq.heappush(component_heaps[root], i)

        res = []
        for typ, x in queries:
            root = find(x)
            if typ == 1:
                if online[x]:
                    res.append(x)
                else:
                    # Find the smallest online station in the component
                    while component_heaps[root] and not online[component_heaps[root][0]]:
                        heapq.heappop(component_heaps[root])
                    if component_heaps[root]:
                        res.append(component_heaps[root][0])
                    else:
                        res.append(-1)
            else:
                online[x] = False

        return res
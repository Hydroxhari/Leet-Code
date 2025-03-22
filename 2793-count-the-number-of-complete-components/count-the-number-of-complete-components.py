class Solution(object):
    def countCompleteComponents(self, n, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Step 2: Helper function to perform BFS and collect nodes in a component
        def bfs(node):
            queue = deque([node])
            visited.add(node)
            component = set()
            
            while queue:
                curr = queue.popleft()
                component.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            return component
        
        # Step 3: Explore all components and check if they are complete
        visited = set()
        complete_components = 0

        for node in range(n):
            if node not in visited:
                # Find all nodes in this component
                component = bfs(node)
                size = len(component)
                
                # Step 4: Check if the component is complete
                # In a complete graph, each node must be connected to all other nodes in the component
                edge_count = sum(len(graph[v]) for v in component) // 2
                if edge_count == size * (size - 1) // 2:
                    complete_components += 1

        return complete_components

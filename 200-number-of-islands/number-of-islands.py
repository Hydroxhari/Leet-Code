class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        island_count = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row, col))

            while queue:
                r, c = queue.popleft()

                # Explore neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n and
                        (nr, nc) not in visited and grid[nr][nc] == '1'):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        # Iterate through the entire grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    island_count += 1  # Found a new island
                    bfs(i, j)          # Explore the entire island

        return island_count

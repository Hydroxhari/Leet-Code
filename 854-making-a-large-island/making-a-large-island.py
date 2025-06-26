class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        island_id = 2  # start from 2 to avoid conflict with 0/1
        area = {}  # island_id -> area size
        visited = set()

        def dfs(i, j, id):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = id
            res = 1
            for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                res += dfs(i + x, j + y, id)
            return res

        # 1. Label islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_id)
                    area[island_id] = size
                    island_id += 1

        max_area = max(area.values() or [0])  # in case grid is full of 1s

        # 2. Try flipping every 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                        ni, nj = i + x, j + y
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])
                    total = 1 + sum(area[id] for id in seen)
                    max_area = max(max_area, total)

        return max_area

from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    q = deque([(i,j)])
                    grid[i][j] = '0'
                    
                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                q.append((nx, ny))
        return count

class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        n, m = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if (
                r < 0 or r >= n or c < 0 or c >= m or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return
            
            visited.add((r, c))

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Start DFS from Pacific edges
        for i in range(n):
            dfs(i, 0, pacific, heights[i][0])        # Left column
            dfs(i, m - 1, atlantic, heights[i][m-1]) # Right column

        for j in range(m):
            dfs(0, j, pacific, heights[0][j])        # Top row
            dfs(n - 1, j, atlantic, heights[n-1][j]) # Bottom row

        # Cells reachable from both oceans
        result = list(pacific & atlantic)
        return result

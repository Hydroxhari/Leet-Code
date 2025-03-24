class Solution(object):
    def uniquePathsWithObstacles(self,grid):
        m, n = len(grid), len(grid[0])
        
        # If the starting or ending cell is an obstacle, return 0
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0
        
        # Initialize a DP table
        dp = [[0] * n for _ in range(m)]
        
        # Starting position
        dp[0][0] = 1
        
        # Fill the first row (considering obstacles)
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if grid[0][j] == 0 else 0
        
        # Fill the first column (considering obstacles)
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if grid[i][0] == 0 else 0
        
        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:  # Only update if there's no obstacle
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]


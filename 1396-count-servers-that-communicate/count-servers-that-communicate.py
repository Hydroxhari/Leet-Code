class Solution(object):
    def countServers(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        points=[]

        row_servers=[0]*rows
        col_servers=[0]*cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    points.append((i,j))
                    row_servers[i]+=1
                    col_servers[j]+=1

        connected=0
        for row,col in points:
            if row_servers[row]>1 or col_servers[col]>1:
                connected+=1
        return connected
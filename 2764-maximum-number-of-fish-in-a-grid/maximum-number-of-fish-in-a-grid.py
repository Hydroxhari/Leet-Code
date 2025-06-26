class Solution(object):
    def findMaxFish(self, grid):

        from collections import deque

        n,m=len(grid),len((grid[0]))

        d=deque()
        v=set()
        me=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]>0 and (i,j) not in v:
                    d.append((i,j))
                    co=0
                    while d:
                        r,c = d.popleft()
                        if (r,c) in v:
                            continue
                        v.add((r,c))
                        co+=grid[r][c]
                        for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                            dx,dy=r+x,c+y
                            if 0<=dx<n and 0<=dy<m and (dx,dy) not in v and grid[dx][dy]>0:
                                d.append((dx,dy))
                    me=max(me,co)
        return me



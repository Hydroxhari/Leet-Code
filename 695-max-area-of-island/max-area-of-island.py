class Solution(object):
    def maxAreaOfIsland(self, g):
        
        m,n=len(g),len(g[0])

        v=set()
        d={(0,1),(1,0),(-1,0),(0,-1)}
        def dfs(i,j,c):
            v.add((i,j))

            for x,y in d:
                ni,nj = i+x,j+y
                if 0<=ni<m and 0<=nj<n and g[ni][nj]==1 and (ni,nj) not in v:
                    c+= dfs(ni,nj,1)
            return c



        a=0
        for i in range(m):
            for j in range(n):
                if g[i][j]==1:
                    if (i,j) in v:
                        continue
                    a=max(a,dfs(i,j,1))
        
        return a

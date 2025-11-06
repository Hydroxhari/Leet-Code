class Solution(object):
    def orangesRotting(self, g):

        t=0
        m,n=len(g),len(g[0])
        d=deque()

        for i in range(m):
            for j in range(n):
                if g[i][j]==1:
                    t+=1
                elif g[i][j]==2:
                    d.append((i,j))
        
        c=0
        sc=0
        while d:
            c+=1
            l=len(d)
            for _ in range(l):
                e=d.popleft()
                i,j=e[0],e[1]
                
                for x,y in {(0,1),(1,0),(0,-1),(-1,0)}:
                    nx,ny=i+x,j+y
                    if 0<=nx<m and 0<=ny<n and g[nx][ny]==1:
                        d.append((nx,ny))
                        sc+=1
                        g[nx][ny]=2
        
        if sc!=t:
            return -1  

        return  0 if c==0 else c-1
class Solution(object):
    def orangesRotting(self, g):

        m,n=len(g),len(g[0])
        o=0
        d=deque()

        for i in range(m):
            for j in range(n):
                if g[i][j]==2:
                    d.append((i,j))
                elif g[i][j]==1:
                    o+=1
        
        t=0
        v=0

        
        if not d and not o:
            return 0

        if not d and o:
            return -1
            
        while d:
            for _ in range(len(d)):
                i,j=d.popleft()
                for x,y in {(0,1),(0,-1),(1,0),(-1,0)}:
                    ni,nj=i+x,j+y
                    if 0<=ni<m and 0<=nj<n and g[ni][nj]==1:
                        g[ni][nj]=2
                        v+=1
                        d.append((ni,nj))
            t+=1
        
        return t-1 if o==v else -1
        



                    

        
class Solution(object):
    def floodFill(self, g, r, c, k):

        m,n=len(g),len(g[0])

        q=deque([(r,c)])
        l = g[r][c]
        if l==k:
            return g
        g[r][c]=k
        d=[(0,1),(1,0),(0,-1),(-1,0)]

        while q:
            i,j = q.popleft()
            for x,y in d:
                ni,nj=x+i,y+j
                if 0<=ni<m and 0<=nj<n and g[ni][nj]==l:
                    g[ni][nj]=k
                    q.append((ni,nj))
        
        return g
        
class Solution(object):
    def numIslands(self, g):
        
        m,n=len(g),len(g[0])
        c=0

        for i in range(m):
            for j in range(n):
                if g[i][j]=='1':
                    c+=1
                    q=deque([(i,j)])
                    g[i][j]='0'
                    while q:
                        a,b = q.popleft()
                        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                            na,nb=x+a,y+b
                            if 0<=na<m and 0<=nb<n and g[na][nb]=='1':
                                g[na][nb]='0'
                                q.append((na,nb))
        return c
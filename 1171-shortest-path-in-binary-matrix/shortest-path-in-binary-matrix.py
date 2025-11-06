class Solution(object):
    def shortestPathBinaryMatrix(self, g):

        m,n=len(g)-1,len(g[0])-1
        c=0
        if g[0][0]!=0:
            return -1
        q=deque([(0,0)])
        d=((1,1),(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1))
        v=set()

        while q:
            l=len(q)
            for _ in range(l):
                i,j=q.popleft()
                if (i,j) in v:
                    continue
                v.add((i,j))
                if (i,j)==(m,n):
                    return c+1
                for x,y in d:
                    nx,ny=i+x,j+y
                    if 0<=nx<=m and 0<=ny<=n and (nx,ny) not in v and g[nx][ny]==0:
                        q.append((nx,ny))
            c+=1
        return -1
class Solution(object):
    def nearestExit(self, g, s):

        d=deque([s])
        m,n=len(g),len(g[0])
        c=0
        v=set()

        while d:
            l=len(d)
            for _ in range(l):

                e = d.popleft()
                i,j=e[0],e[1]
                if (i,j) in v:
                    continue
                v.add((i,j))

                if (i==0 or i==m-1 or j==0 or j==n-1) and [i,j]!=s:
                    return c

                for x,y in {(0,1),(1,0),(-1,0),(0,-1)}:
                    nx,ny=x+i,y+j
                    if 0<=nx<m and 0<=ny<n and g[nx][ny]!='+' and (nx,ny) not in v:
                        d.append([nx,ny])
            c+=1

        return -1
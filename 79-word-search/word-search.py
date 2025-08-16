class Solution(object):
    def exist(self, b, w):
        
        d={(0,1),(1,0),(-1,0),(0,-1)}

        def dp(i,j,wi,s):
            if wi==len(w):
                return True
            it=False
            for x,y in d:
                ni,nj=x+i,y+j
                if 0<=ni<m and 0<=nj<n and b[ni][nj]==w[wi] and (ni,nj) not in s:
                    s.add((ni,nj))
                    it=it or dp(ni,nj,wi+1,s)
                    s.remove((ni,nj))
            return it                 
        
        
        m,n=len(b),len(b[0])
        ot=False

        for i in range(m):
            for j in range(n):
                if b[i][j]==w[0]:
                    ot= ot or dp(i,j,1,{(i,j)})
        return ot

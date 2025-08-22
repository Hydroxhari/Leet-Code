class Solution(object):
    def minimumArea(self, g):

        sx,sy,ex,ey=float('inf'),float('inf'),0,0

        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j]==1:
                    sx=min(sx,i)
                    sy=min(sy,j)
                    ex=max(ex,i)
                    ey=max(ey,j)
        
        l=ex-sx+1
        b=ey-sy+1
        return l*b
        
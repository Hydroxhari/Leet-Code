class Solution(object):
    def rotate(self, g):

        l=len(g)

        for i in range(l):
            for j in range(i+1,l):
                g[i][j],g[j][i]=g[j][i],g[i][j]
        
        for i in range(l):
            g[i]=g[i][::-1]
        
        

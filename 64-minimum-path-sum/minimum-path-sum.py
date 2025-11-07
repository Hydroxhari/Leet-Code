class Solution(object):
    def minPathSum(self, g):

        n=[[0 for _ in range(len(g[0]))] for _ in range(len(g))]

        n[0][0]=g[0][0]
        for i in range(1,len(g)):
            n[i][0]=n[i-1][0]+g[i][0]
        for j in range(1,len(g[0])):
            n[0][j]=n[0][j-1]+g[0][j]
        
        for i in range(1,len(g)):
            for j in range(1,len(g[0])):
                n[i][j]=g[i][j]+min(n[i-1][j],n[i][j-1])
        return n[-1][-1]

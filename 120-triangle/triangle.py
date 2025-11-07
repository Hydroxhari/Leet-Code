class Solution(object):
    def minimumTotal(self, t):

        for i in range(1,len(t)):
            for j in range(i+1):
                if j==0:
                    t[i][j]+=t[i-1][j]
                elif j==i:
                    t[i][j]+=t[i-1][j-1]
                else:
                    t[i][j]+=min(t[i-1][j-1],t[i-1][j])
        
        return min(t[-1])


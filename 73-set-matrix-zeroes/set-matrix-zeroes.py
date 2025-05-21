class Solution(object):
    def setZeroes(self, m):
        n,k=len(m),len(m[0])
        r=set()
        c=set()
        for i in range(n):
            for j in range(k):
                if m[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in range(n):
            for j in range(k):
                if i in r or j in c:
                    m[i][j]=0
        print(n)
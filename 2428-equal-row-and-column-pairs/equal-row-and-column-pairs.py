class Solution(object):
    def equalPairs(self, g):

        r=defaultdict(int)
        m,n=len(g),len(g[0])

        for i in range(m):
            nu=''
            for j in range(n):
                nu+=str(g[i][j])+'!'
            r[nu]+=1

        c=defaultdict(int)
        for i in range(n):
            nu=''
            for j in range(m):
                nu+=str(g[j][i])+'!'
            c[nu]+=1
        
        a=0
        for i,j in r.items():
            if i in c:
                a+=j*c[i]
        return a

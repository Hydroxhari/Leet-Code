class Solution(object):
    def equalPairs(self, g):

        d=defaultdict(int)
        for i in g:
            d[tuple(i)]+=1
        
        c=0
        for i in range(len(g)):
            l=[]
            for j in range(len(g)):
                l.append(g[j][i])
            c+=1*d[tuple(l)]
        return c

        
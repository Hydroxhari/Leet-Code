class Solution(object):
    def findOrder(self, n, pre):

        g=defaultdict(list)
        l=[]

        for i,j in pre:
            g[i].append(j)
        
        v=set()
        p=set()

        def dfs(i):
            if i in v:
                return 
            
            v.add(i)
            p.add(i)
            for j in g[i]:
                if j in p:
                    return 
                if j not in v:
                    dfs(j)
            p.remove(i)
            l.append(i)
            return

        for i in range(n):
            if i not in v:
                dfs(i)
        
        return l if len(l)==n else []
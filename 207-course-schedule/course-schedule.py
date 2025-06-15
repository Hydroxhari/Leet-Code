class Solution(object):
    def canFinish(self, n, p):

        d=defaultdict(list)

        for i,j in p:
            d[i].append(j)
        
        v=set()

        def dfs(i):
            if i in v:
                return False
            if d[i]==[]:
                return True
            
            v.add(i)
            for j in d[i]:
                if not dfs(j):
                    return False
            
            v.remove(i)
            d[i]=[]
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        
        return True
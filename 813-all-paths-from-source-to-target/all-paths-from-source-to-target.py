class Solution(object):
    def allPathsSourceTarget(self, g):

        d=defaultdict(list)
        for i in range(len(g)):
            for j in g[i]:
                d[i].append(j)

        q=deque([(0,[0])])
        ans=[]
        while q:
            n,l=q.popleft()
            if n==len(g)-1:
                ans.append(l)
                continue
            
            for nei in d[n]:
                q.append((nei,l+[nei]))

        return ans
class Solution(object):
    def findOrder(self, n, p):

        d=defaultdict(list)
        a=[0]*n
        for i,j in p:
            d[j].append(i)
            a[i]+=1
        
        q=deque([i for i in range(n) if a[i]==0])

        ans=[]
        c=0
        while q:
            e=q.popleft()
            c+=1
            ans.append(e)
            for nei in d[e]:
                a[nei]-=1
                if a[nei]==0:
                    q.append(nei)
        
        return ans if c==n else []

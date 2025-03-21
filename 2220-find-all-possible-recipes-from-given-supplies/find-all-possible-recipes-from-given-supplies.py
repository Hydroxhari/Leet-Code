class Solution(object):
    def findAllRecipes(self, r, i, s):

        d=defaultdict(list)
        ind={ir:0 for ir in r}
        a=set(s)

        for x,y in zip(r,i):
            for z in y:
                if z not in a:
                    ind[x]+=1
                    d[z].append(x)
        
        q=deque([j for j in ind if ind[j]==0])
        f=[]

        while q:
            e=q.popleft()
            f.append(e)

            for j in d[e]:
                ind[j]-=1
                if ind[j]==0:
                    q.append(j)
        
        return f

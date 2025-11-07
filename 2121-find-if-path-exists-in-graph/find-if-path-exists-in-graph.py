class Solution(object):
    def validPath(self, n, e, s, d):

        g=defaultdict(list)
        for i,j in e:
            g[i].append(j)
            g[j].append(i)
        
        q=deque([s])
        v=set()
        while q:
            x=q.popleft()
            if x==d:
                return True
            if x in v:
                continue
            v.add(x)
            for nei in g[x]:
                if nei not in v:
                    q.append(nei)
        return False